/**
 * End-to-end test for CJK search support.
 * 
 * Verifies that:
 * 1. The search index file is valid and includes CJK tokens in the elasticlunr trie
 * 2. The runtime tokenizer patch correctly splits CJK query terms
 * 3. Combined: patched tokenizer + CJK trie entries → correct search results
 * 
 * Usage: node scripts/e2e-test.js
 * Requires: mdbook build + cjk-search.js to have been run first.
 */
const fs = require('fs');
const path = require('path');

const BOOK_DIR = path.resolve('_book');

// -----------------------------------------------------------------------
// Find search index file
// -----------------------------------------------------------------------
function findSearchIndexFile() {
    const files = fs.readdirSync(BOOK_DIR)
        .filter(f => f.startsWith('searchindex-') && f.endsWith('.js'))
        .sort();
    if (files.length === 0) {
        throw new Error('No searchindex-*.js found. Run mdbook build + cjk-search.js first.');
    }
    return path.join(BOOK_DIR, files[files.length - 1]);
}

// -----------------------------------------------------------------------
// Simulate elasticlunr tokenizer with CJK patch
// -----------------------------------------------------------------------
const CJK_RE = /([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef])/g;
const SEPARATOR = /[\s\-]+/;

function tokenize(str) {
    if (!str) return [];
    const tokens = str.trim().toLowerCase();
    // Insert spaces before each CJK character (simulates the runtime patch)
    const spaced = tokens.replace(CJK_RE, ' $1 ').trim();
    return spaced.split(SEPARATOR).filter(t => t !== '');
}

// -----------------------------------------------------------------------
// Simulate elasticlunr search on the trie
// -----------------------------------------------------------------------
function searchTrie(root, term) {
    // For single CJK character, look it up directly in root
    if (root[term]) {
        const entry = root[term];
        const docIds = Object.keys(entry.docs || {});
        return docIds.map(id => ({ docId: id, score: entry.df || 1 }));
    }
    return [];
}

function searchIndex(data, queryStr) {
    const tokens = tokenize(queryStr);
    const results = {};

    for (const token of tokens) {
        for (const field of ['body', 'title', 'breadcrumbs']) {
            const fieldIdx = data.index.index[field];
            if (!fieldIdx) continue;
            
            const matches = searchTrie(fieldIdx.root, token);
            for (const m of matches) {
                if (!results[m.docId]) {
                    results[m.docId] = { docId: m.docId, matches: [] };
                }
                results[m.docId].matches.push({ field, token });
            }
        }
    }

    return Object.values(results).sort((a, b) => b.matches.length - a.matches.length);
}

// -----------------------------------------------------------------------
// Main
// -----------------------------------------------------------------------
function main() {
    const indexFile = findSearchIndexFile();
    console.log(`📖 Index: ${path.basename(indexFile)}`);
    console.log(`   Size: ${(fs.statSync(indexFile).size / 1024 / 1024).toFixed(1)} MB`);

    // Load the search index
    const vm = require('vm');
    const sandbox = { window: { search: {} } };
    new vm.Script(fs.readFileSync(indexFile, 'utf8')).runInContext(vm.createContext(sandbox));
    const data = sandbox.window.search;
    const docStore = data.index.documentStore.docs || {};

    console.log(`📚 Documents: ${Object.keys(docStore).length}`);
    
    // Check CJK tokens in each field
    let passed = 0, failed = 0;

    // Test 1: CJK tokens exist in the body trie
    console.log('\n--- Test 1: CJK tokens in trie ---');
    const bodyRoot = data.index.index.body.root;
    const cjkKeys = Object.keys(bodyRoot).filter(k => k.length === 1 && 
        [...k].some(c => {
            const cp = c.codePointAt(0);
            return (cp >= 0x4E00 && cp <= 0x9FFF) || (cp >= 0x3400 && cp <= 0x4DBF);
        }));
    console.log(`   CJK tokens in body: ${cjkKeys.length}`);
    if (cjkKeys.length > 1000) {
        console.log(`   ✅ PASS (${cjkKeys.length} CJK tokens found)`);
        passed++;
    } else {
        console.log(`   ❌ FAIL (expected > 1000, got ${cjkKeys.length})`);
        failed++;
    }

    // Test 2: Tokenizer splits CJK correctly
    console.log('\n--- Test 2: CJK tokenizer ---');
    const testQueries = [
        ['侦察', ['侦', '察']],
        ['渗透测试', ['渗', '透', '测', '试']],
        ['attack', ['attack']],
        ['T1059', ['t1059']],
        ['侦察 attack', ['侦', '察', 'attack']],
    ];
    for (const [query, expected] of testQueries) {
        const tokens = tokenize(query);
        const ok = JSON.stringify(tokens) === JSON.stringify(expected);
        console.log(`   "${query}" → [${tokens}] ${ok ? '✅' : '❌'}`);
        if (ok) passed++; else failed++;
    }

    // Test 3: Search yields results for CJK terms
    console.log('\n--- Test 3: CJK search results ---');
    const searchTerms = ['侦', '攻击', '渗透', '侦察'];
    for (const term of searchTerms) {
        const tokens = tokenize(term);
        const results = searchIndex(data, term);
        const hasResults = results.length > 0;
        console.log(`   "${term}" (tokens: [${tokens}]) → ${results.length} docs ${hasResults ? '✅' : '❌'}`);
        if (hasResults) {
            passed++;
            // Show top result
            const top = results[0];
            const doc = docStore[top.docId];
            if (doc) {
                console.log(`     Top: doc#${top.docId} "${doc.title?.substring(0, 60)}"`);
            }
        } else {
            failed++;
        }
    }

    // Test 4: Multi-character CJK search (AND semantics)
    console.log('\n--- Test 4: Multi-char CJK search ---');
    // Split "侦察" into ["侦", "察"], find docs containing both
    const qTokens = tokenize('侦察');
    let allResults = null;
    for (const token of qTokens) {
        const results = searchIndex(data, token);
        const docIds = new Set(results.map(r => r.docId));
        if (allResults === null) {
            allResults = docIds;
        } else {
            allResults = new Set([...allResults].filter(id => docIds.has(id)));
        }
    }
    const multiCharResults = allResults ? allResults.size : 0;
    console.log(`   "侦察" (AND of 侦+察) → ${multiCharResults} docs matching BOTH chars`);
    if (multiCharResults > 0) {
        console.log('   ✅ PASS');
        passed++;
    } else {
        console.log('   ❌ FAIL');
        failed++;
    }

    // Summary
    console.log('\n========================================');
    console.log(`Results: ${passed} passed, ${failed} failed, ${passed + failed} total`);
    console.log('========================================');

    process.exit(failed > 0 ? 1 : 0);
}

main();
