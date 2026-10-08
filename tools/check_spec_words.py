"""Check that Beluma words in backticks of spec/*.md exist in lexicon/h.txt."""
import re, glob, sys, unicodedata

def strip(w):
    return ''.join(c for c in unicodedata.normalize('NFD', w.lower()) if c not in '\u0300\u0301')

def load_keys(path='lexicon/h.txt'):
    keys = set()
    for ln in open(path, encoding='utf-8'):
        s = ln.strip()
        if s and not s.startswith('#'):
            m = re.match(r'^([^:=\[\]]+?)\s*[:=]', s)
            if m:
                keys.add(strip(m.group(1).strip()))
    return keys

AFFIX = set('la s as va ke ke ji or et os an pira tavi ik le le nira sula nel un ni re'.split())
GRAM = set('mi mu tu nivo siva et mis tur misu eka oka ta lé o s un du ne we wes kvo kwa kva kvasi kwaras kvado kvaso havi kek non unas ora neka'.split())
# tokens that are meta-linguistic notation, not Beluma words
ALLOW = set('im in cv cvv cvcv ks sp dizaésita mala ksa parentesa dota kama tuo-dota dota-kama sa-morka morka-nira linya-nira linya-sula dota-tro linya-ora na-morka linya-dis porsenta-morka kris-morka ré'.split())

def derivative_ok(w, keys):
    if w.startswith('-') or len(w) <= 2:
        return True
    if w.endswith('-'):
        w = w.rstrip('-')
    if w in ALLOW:
        return True
    for pre in ('ré-', 'un-', 'ni-'):
        if w.startswith(pre) and len(w) > 3:
            if derivative_ok(w[3:], keys):
                return True
    if strip(w) in keys or w in AFFIX or w in GRAM:
        return True
    # root used inside any hyphenated dictionary key (e.g. jula in kora-jula)
    for k in keys:
        if '-' in k and w in k.split('-'):
            return True
    for suf in ['nélo', 'nira', 'sula', 'pira', 'tavi', 'morka', 'ké', 'ke', 'va', 'la', 'as', 'ji', 'lé', 's']:
        if w.endswith(suf) and len(w) > len(suf) and derivative_ok(w[:-len(suf)], keys):
            return True
    if '-' in w:
        parts = w.split('-')
        if all(strip(p) in keys or p in AFFIX or p in GRAM for p in parts):
            return True
    for i in range(1, len(w)):
        if strip(w[:i]) in keys and strip(w[i:]) in keys:
            return True
    return False

def main():
    keys = load_keys()
    bad = {}
    files = sorted(glob.glob('spec/*.md')) or sys.argv[1:]
    for f in files:
        txt = open(f, encoding='utf-8').read()
        for w in re.findall(r'`([a-z\u00e1\u00e9\u00ed\u00f3\u00fa\-]+)`', txt.lower()):
            if not derivative_ok(w, keys):
                bad.setdefault(w, set()).add(f.replace('\\', '/').split('/')[-1])
    for w in sorted(bad):
        print(f'{w} -> {sorted(bad[w])}')
    print(f'TOTAL unknown: {len(bad)}')
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())
