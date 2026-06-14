/**
 * CJK Search Index Post-Processor for mdBook
 * 
 * Parses the mdBook search index, adds CJK (Chinese/Japanese/Korean) character
 * tokens to the elasticlunr trie, and re-serializes the index.
 * 
 * This enables CJK full-text search by splitting Chinese text into individual
 * character tokens, working in tandem with theme/cjk-search.js which patches
 * the elasticlunr tokenizer at runtime to split CJK query terms into characters.
 * 
 * Usage: node scripts/cjk-search.js [--book-dir ./_book] [--dry-run]
 * 
 * Pipeline: mdbook build && node scripts/cjk-search.js
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

// ---------------------------------------------------------------------------
// CJK Unicode Ranges
// ---------------------------------------------------------------------------
const CJK_RANGES = [
    [0x2E80, 0x2EFF], // CJK Radicals Supplement
    [0x2F00, 0x2FDF], // Kangxi Radicals
    [0x3040, 0x309F], // Hiragana
    [0x30A0, 0x30FF], // Katakana
    [0x3100, 0x312F], // Bopomofo
    [0x3200, 0x32FF], // Enclosed CJK Letters
    [0x3400, 0x4DBF], // CJK Unified Ideographs Extension A
    [0x4E00, 0x9FFF], // CJK Unified Ideographs
    [0xF900, 0xFAFF], // CJK Compatibility Ideographs
    [0xFF00, 0xFFEF], // Fullwidth Forms
];

function isCJKChar(cp) {
    return CJK_RANGES.some(([lo, hi]) => cp >= lo && cp <= hi);
}

function extractCJKChars(text) {
    const chars = new Set();
    for (const c of text) {
        if (isCJKChar(c.codePointAt(0))) chars.add(c);
    }
    return chars;
}

// ---------------------------------------------------------------------------
// JS string literal escaping (for wrapping JSON in JSON.parse('...'))
// ---------------------------------------------------------------------------
function jsEscape(str) {
    return str
        .replace(/\\/g, '\\\\')
        .replace(/'/g, "\\'");
}

// ---------------------------------------------------------------------------
// Search index file discovery
// ---------------------------------------------------------------------------
function findSearchIndexFile(bookDir) {
    const files = fs.readdirSync(bookDir)
        .filter(f => f.startsWith('searchindex-') && f.endsWith('.js'))
        .sort();
    if (files.length === 0) {
        throw new Error(`No searchindex-*.js found in ${bookDir}. Run 'mdbook build' first.`);
    }
    return path.join(bookDir, files[files.length - 1]);
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
function main() {
    const args = process.argv.slice(2);
    let bookDir = '_book';
    let dryRun = false;

    for (let i = 0; i < args.length; i++) {
        if (args[i] === '--book-dir' && i + 1 < args.length) {
            bookDir = args[i + 1];
            i++;
        } else if (args[i] === '--dry-run') {
            dryRun = true;
        }
    }

    bookDir = path.resolve(bookDir);
    const indexFile = findSearchIndexFile(bookDir);

    console.log(`📖 Index file: ${path.basename(indexFile)}`);
    console.log(`   Size: ${(fs.statSync(indexFile).size / 1024 / 1024).toFixed(1)} MB`);

    // -----------------------------------------------------------------------
    // 1. Parse the search index JS file
    // -----------------------------------------------------------------------
    const rawContent = fs.readFileSync(indexFile, 'utf8');

    const sandbox = { window: { search: {} } };
    new vm.Script(rawContent).runInContext(vm.createContext(sandbox));
    const data = sandbox.window.search;

    const docStore = data.index.documentStore.docs || {};
    const invIdx = data.index.index;
    const fields = ['body', 'title', 'breadcrumbs'].filter(f => invIdx[f]);

    console.log(`📚 Documents: ${Object.keys(docStore).length}`);
    console.log(`🔍 Fields: ${fields.join(', ')}`);

    // -----------------------------------------------------------------------
    // 2. Build CJK char → docId set map from document store
    // -----------------------------------------------------------------------
    let totalNewTokens = 0;

    for (const fieldName of fields) {
        const fieldIdx = invIdx[fieldName];
        const root = fieldIdx.root;

        // Collect CJK characters from all documents for this field
        const charDocMap = new Map();
        for (const [docId, doc] of Object.entries(docStore)) {
            const text = doc[fieldName];
            if (typeof text !== 'string' || text.length === 0) continue;
            for (const ch of extractCJKChars(text)) {
                if (!charDocMap.has(ch)) charDocMap.set(ch, new Set());
                charDocMap.get(ch).add(docId);
            }
        }

        // Filter out characters already in the trie
        const existingChars = new Set(Object.keys(root));
        const charsToAdd = [...charDocMap.entries()]
            .filter(([ch]) => !existingChars.has(ch));

        console.log(`\n  Field '${fieldName}':`);
        console.log(`    Unique CJK chars: ${charDocMap.size}`);
        console.log(`    Already indexed: ${charDocMap.size - charsToAdd.length}`);
        console.log(`    New tokens: ${charsToAdd.length}`);

        if (charsToAdd.length === 0) {
            console.log(`    ✅ All CJK chars already indexed`);
            continue;
        }

        // Add tokens to the trie
        // Order doc IDs ascending for compact JSON representation
        const sortedDocIds = [...charsToAdd].map(([ch, ids]) => [ch, [...ids].sort((a, b) => +a - +b)]);
        for (const [ch, ids] of sortedDocIds) {
            const docs = {};
            for (const docId of ids) {
                docs[docId] = { tf: 1 };
            }
            root[ch] = { docs, df: ids.length };
        }

        totalNewTokens += charsToAdd.length;
        console.log(`    ✅ Added ${charsToAdd.length} tokens`);
    }

    if (totalNewTokens === 0) {
        console.log(`\n✅ No new CJK tokens needed`);
        return;
    }

    // -----------------------------------------------------------------------
    // 3. Re-serialize and wrap in JS
    // -----------------------------------------------------------------------
    console.log(`\n📦 Re-serializing index...`);

    const newJson = JSON.stringify(data);
    const newJs = jsEscape(newJson);
    const newContent =
        `window.search = Object.assign(window.search, JSON.parse('${newJs}'));`;

    const origSize = rawContent.length;
    const newSize = newContent.length;
    const deltaMb = ((newSize - origSize) / 1024 / 1024).toFixed(2);

    console.log(`   Original: ${(origSize / 1024 / 1024).toFixed(2)} MB`);
    console.log(`   New:      ${(newSize / 1024 / 1024).toFixed(2)} MB`);
    console.log(`   Delta:    ${deltaMb > 0 ? '+' : ''}${deltaMb} MB`);

    if (dryRun) {
        console.log(`\n✅ Dry run: would add ${totalNewTokens} CJK tokens (${deltaMb} MB delta)`);
        return;
    }

    // -----------------------------------------------------------------------
    // 4. Write and verify
    // -----------------------------------------------------------------------
    fs.writeFileSync(indexFile, newContent, 'utf8');

    // Verify: re-parse and check CJK tokens
    try {
        const verify = { window: { search: {} } };
        new vm.Script(newContent).runInContext(vm.createContext(verify));
        const vIdx = verify.window.search.index.index;

        let verified = 0;
        for (const fieldName of fields) {
            const vRoot = vIdx[fieldName].root;
            const cjkInRoot = Object.keys(vRoot)
                .filter(k => k.length === 1 && isCJKChar(k.codePointAt(0)));
            verified += cjkInRoot.length;
        }

        console.log(`\n✅ Verification: file parses correctly`);
        console.log(`📊 CJK tokens in index: ${verified}`);

        // Verify a few specific CJK characters are present in the trie
        const bodyRoot = vIdx.body.root;
        const sampleChars = ['侦', '攻', '击', '渗', '透'];
        for (const ch of sampleChars) {
            if (bodyRoot[ch]) {
                console.log(`   ✓ "${ch}": ${bodyRoot[ch].df} docs`);
            } else {
                console.log(`   ✗ "${ch}": NOT FOUND`);
            }
        }

        console.log(`\n✅ CJK search index updated successfully`);
        console.log(`   New size: ${(fs.statSync(indexFile).size / 1024 / 1024).toFixed(1)} MB`);
    } catch (e) {
        console.log(`\n❌ Verification failed: ${e.message}`);
        console.log(`   Restoring original...`);
        fs.writeFileSync(indexFile, rawContent, 'utf8');
        process.exit(1);
    }
}

main();
