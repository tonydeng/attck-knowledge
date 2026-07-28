/**
 * CJK Search Support for mdBook
 * 
 * Patches elasticlunr.js tokenizer to handle Chinese/Japanese/Korean text.
 * CJK characters are split individually so each character becomes its own token.
 * Combined with the expanded search index (from scripts/cjk-search.js post-processing),
 * this enables character-level CJK full-text search.
 * 
 * Works with: mdBook 0.4.x / 0.5.x (elasticlunr-based search)
 */
(function cjkSearch() {
    'use strict';

    // Wait for elasticlunr to be available
    function patchTokenizer() {
        if (typeof elasticlunr === 'undefined' || !elasticlunr.tokenizer) {
            // elasticlunr not loaded yet, retry
            setTimeout(patchTokenizer, 100);
            return;
        }

        // CJK character ranges (see regex below for actually covered ranges):
        //   U+2E80-U+2EFF  CJK Radicals Supplement
        //   U+2F00-U+2FDF  Kangxi Radicals
        //   U+3040-U+309F  Hiragana (Japanese)
        //   U+30A0-U+30FF  Katakana (Japanese)
        //   U+3100-U+312F  Bopomofo (Chinese phonetic)
        //   U+3200-U+32FF  Enclosed CJK
        //   U+3400-U+4DBF  CJK Unified Ideographs Extension A
        //   U+4E00-U+9FFF  CJK Unified Ideographs (most common)
        //   U+F900-U+FAFF  CJK Compatibility Ideographs
        //   U+FF00-U+FFEF  Fullwidth forms
        // Note: U+3000-U+303F (CJK Symbols and Punctuation) intentionally excluded
        //       to avoid splitting on fullwidth punctuation (e.g. 。，、)

        // Override the default separator to insert zero-width boundary before
        // each CJK character, so elasticlunr treats them as individual tokens.
        // The default separator is /[\s\-]+/
        // We need to split on whitespace/hyphens AND between CJK characters.
        //
        // Strategy: override tokenizer.seperator and also provide a custom
        // tokenizer function that handles CJK splitting.

        var defaultSeparator = elasticlunr.tokenizer.seperator ||
            /[\s\-]+/;

        // Create a custom tokenizer that splits CJK into individual chars
        var originalTokenizer = elasticlunr.tokenizer;

        elasticlunr.tokenizer = function (str) {
            if (!arguments.length || str === null || str === undefined) {
                return [];
            }

            var tokens;
            if (typeof str === 'string') {
                tokens = str.trim().toLowerCase();
            } else {
                tokens = elasticlunr.utils.toString(str).toLowerCase();
            }

            // Insert zero-width space before each CJK character, then split
            // This effectively makes each CJK character its own token
            tokens = tokens.replace(
                /([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef])/g,
                ' $1 '
            ).trim();

            // Now split by the separator (whitespace/hyphen)
            return tokens.split(defaultSeparator).filter(function (t) {
                return t !== '';
            });
        };

        // Copy over static properties
        elasticlunr.tokenizer.defaultSeperator = defaultSeparator;
        elasticlunr.tokenizer.seperator = defaultSeparator;

        console.log('[CJK Search] Tokenizer patched for CJK support');
    }

    // Hook into the page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', patchTokenizer);
    } else {
        patchTokenizer();
    }
})();
