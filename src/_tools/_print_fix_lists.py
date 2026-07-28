"""打印各类修复清单 - 供主智能体审视"""
import json
from pathlib import Path

BASE = Path(__file__).parent.parent / '_data' / '_fix_lists'

for cat in ['missing_parents', 'extra_parents', 'name_mismatch_parents',
            'missing_subs', 'extra_subs', 'name_mismatch_subs']:
    with open(BASE / f'{cat}.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
    print(f'\n=== {cat} ({len(items)}) ===')
    for it in items:
        tid = it.get('tid', '?')
        local = it.get('local_name', '')
        official = it.get('official_name', '')
        f = it.get('local_file', '')
        tactic = it.get('_tactic_dir', '')
        if cat == 'name_mismatch_parents' or cat == 'name_mismatch_subs':
            print(f'  [{tactic}] {tid} | local={local!r} -> official={official!r} | file={f}')
        else:
            print(f'  [{tactic}] {tid} | name={local or official!r} | file={f}')
