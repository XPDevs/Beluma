"""grow.py - compute Beluma's reachable-lexicon capacity and emit candidates.

Usage:
  python tools/grow.py capacity          # report combinatorial capacity
  python tools/grow.py derive ROOT       # list licensed derivations of ROOT
  python tools/grow.py compounds HEAD    # list registered+licensed HEAD compounds
"""
import re
import sys
import io
import unicodedata

if sys.stdout.encoding and 'utf' not in sys.stdout.encoding.lower():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DERIV = {
    # prefix
    'un-': 'not', 'ni-': 'opposite', 'ré-': 'again', 'né-': 'before',
    'wé-': 'after', 'mi-': 'between', 'hi-': 'over', 'lu-': 'under',
    'ko-': 'with', 'dis-': 'across', 'zu-': 'bad', 'gavo-': 'good',
    # noun
    '-or': 'doer', '-pira': 'tool', '-tavi': 'platform', '-tiva': 'room',
    '-nása': 'house/institution', '-an': 'place', '-os': 'collective',
    '-ét': 'young', '-ik': 'resembling', '-va': 'act', '-ké': 'result',
    '-sula': 'great/abstract', '-nira': 'small', '-moka': 'outside',
    '-nilo': 'inside', '-síka': 'piece', '-kosa': 'state',
    # adjective
    '-oka': 'having', '-uma': 'lacking', '-vela': 'full of', '-sama': 'like',
    '-ona': 'made of', '-jan': 'able', '-jira': 'worthy',
    # verb
    '-ka': 'causative', '-ta': 'become', '-sa': 'produce', '-ni': 'by means of',
    '-ruka': 'repetitive', '-ski': 'attempt', '-bira': 'malefactive',
}

# rough semantic-field estimates for capacity (roots are counted from the dict)
HEADS = 500
MODIFIERS = 2000
DERIV_PER_ROOT = len(DERIV)


def load():
    entries = {}
    for raw in open('lexicon/h.txt', encoding='utf-8'):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        m = re.match(r'^(.+?)\s*=\s*(.+)$', line)
        if m:
            entries[m.group(1).strip()] = m.group(2).strip()
    return entries


def capacity():
    e = load()
    roots = [k for k in e if ' ' not in k]
    r = len(roots)
    derived = r * DERIV_PER_ROOT
    print(f'roots/words registered : {r}')
    print(f'derivation affixes     : {DERIV_PER_ROOT}')
    print(f'-> derivable words     : {derived:,}')
    print(f'head classes (est.)    : {HEADS}')
    print(f'modifiers (est.)       : {MODIFIERS}')
    print(f'-> 2-part compound space: {HEADS * MODIFIERS:,}')
    print(f'-> reachable total (est): {derived + HEADS * MODIFIERS:,}')
    print(f'target v1.0 registered : 20,000+')
    print(f'target capacity        : 250,000+  '
          f'({">= met" if derived + HEADS * MODIFIERS >= 250000 else "short"})')


def derive(root):
    e = load()
    if root not in e:
        print(f'{root!r} is not a registered root'); return
    print(f'{root} = {e[root]}')
    for aff, meaning in DERIV.items():
        print(f'  {root}{aff:<8} {meaning}' if aff.endswith('-')
              else f'  {root}{aff:<8} {meaning}')


def compounds(head):
    e = load()
    heads = [head] if head in e else [k for k in e if head in k]
    for h in heads:
        print(f'{h} = {e[h]}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        capacity()
    elif sys.argv[1] == 'capacity':
        capacity()
    elif sys.argv[1] == 'derive' and len(sys.argv) > 2:
        derive(sys.argv[2])
    elif sys.argv[1] == 'compounds' and len(sys.argv) > 2:
        compounds(sys.argv[2])
    else:
        print(__doc__)
