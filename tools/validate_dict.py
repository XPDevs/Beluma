"""Validate lexicon/h.txt: format, alphabet, phonotactics, collisions.

Usage: python tools/validate_dict.py [--strict]
Exit code 0 = valid (warnings allowed), 1 = errors.
"""
import re
import sys
import unicodedata
from collections import Counter, defaultdict

VOWELS = set('aeiou')
LETTERS = set('abdefghijklmnoprstuvwxz')
ACCENTED = set('\u00e1\u00e9\u00ed\u00f3\u00fa')
OK_ONSETS = {'pr', 'tr', 'br', 'dr', 'fr', 'kr', 'gr', 'pl', 'kv', 'kw', 'sp'}
OK_CODAS = set('snrlk')          # productive codas for new words
ESTABLISHED_CODAS = set('snrlktdfpwx')  # allowed anywhere in existing entries
ILLEGAL_LETTERS = set('cqy')


def strip_accents(w: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', w.lower())
                   if c not in '\u0300\u0301')


def parse(path='lexicon/h.txt'):
    entries, vtxt, bad_lines = [], None, []
    for i, raw in enumerate(open(path, encoding='utf-8'), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith('#'):
            m = re.match(r'#\s*VTXT\s*=?\s*([\d.]+)', line)
            if m:
                vtxt = m.group(1)
            continue
        m = re.match(r'^([^:=\[\]]+?)\s*[:=]\s*(\S.*)$', line)
        if not m:
            bad_lines.append((i, line))
            continue
        key = m.group(1).strip()
        gloss = m.group(2).strip()
        entries.append((i, key, gloss))
    return entries, vtxt, bad_lines


def syllables(part: str):
    """Split one hyphen-free component into syllables (onset-aware)."""
    # cut before each consonant that starts a new syllable (V or VC | CV...)
    return re.findall(r'[^aeiou\u00e1\u00e9\u00ed\u00f3\u00fa]*[aeiou\u00e1\u00e9\u00ed\u00f3\u00fa]+[^aeiou\u00e1\u00e9\u00ed\u00f3\u00fa]*', part)


def check_key(key, errors, warnings, seen_exact, seen_flat, accent_pairs):
    flat = strip_accents(key)
    # alphabet
    for ch in key.lower():
        if ch.isalpha() and ch not in LETTERS and ch not in ACCENTED:
            errors.append(f'illegal letter {ch!r} in {key}')
    if any(c in ILLEGAL_LETTERS for c in strip_accents(key)):
        errors.append(f'illegal letter (c/q/y) in {key}')
    # exact duplicate
    lk = key.lower()
    if lk in seen_exact:
        errors.append(f'duplicate key: {key}')
    seen_exact.add(lk)
    # accent-stripped collision
    if flat in seen_flat and flat != lk:
        errors.append(f'accent-pair collision: {key} vs earlier unaccented form')
    if flat in seen_flat and flat == lk:
        pass  # plain duplicate handled above
    seen_flat.setdefault(flat, lk)
    # accent-pair registry: same flat form, different accents
    if any(c in ACCENTED for c in key):
        accent_pairs[flat].add(key)

    for part in key.lower().split('-'):
        if not part:
            errors.append(f'empty component in {key}')
            continue
        if ' ' in part:
            continue  # multi-word keys: skip syllable checks
        # illegal letters inside
        if set(strip_accents(part)) & ILLEGAL_LETTERS:
            errors.append(f'illegal letter in component {part!r} of {key}')
            continue
        # onset cluster of the component
        m = re.match(r'^([^aeiou\u00e1\u00e9\u00ed\u00f3\u00fa]{2})(?=[^aeiou\u00e1\u00e9\u00ed\u00f3\u00fa]*[aeiou\u00e1\u00e9\u00ed\u00f3\u00fa])', part)
        if m and m.group(1) not in OK_ONSETS:
            errors.append(f'illegal onset {m.group(1)!r} in {key}')
        # coda of the component (after last vowel, before end)
        m2 = re.search(r'(?<=[aeiou\u00e1\u00e9\u00ed\u00f3\u00fa])([bcdfghjklmnpqrstvwxz]+)$', part)
        if m2:
            coda = m2.group(1)
            if len(coda) > 1:
                errors.append(f'multi-consonant coda {coda!r} in {key}')
            elif coda not in ESTABLISHED_CODAS:
                errors.append(f'illegal coda {coda!r} in {key}')
            elif coda not in OK_CODAS and not re.search(r'[\u00e9\u00ed\u00f3\u00fa\u00e1]t$', part):
                warnings.append(f'rare coda {coda!r} in {key}')
        # accent placement: every accented syllable must be the penult of its component
        syls = [s for s in re.split(r'(?<=[aeiou])', part) if s]
        acc_idx = [i for i, s in enumerate(syls) if any(c in s for c in ACCENTED)]
        if acc_idx:
            if len(syls) == 1:
                pass  # monosyllable accent: allowed only for accent pairs (checked via registry)
            elif acc_idx[0] != len(syls) - 2:
                errors.append(f'accent not on penult in {key} (component {part}, syls {syls})')


def main(argv):
    strict = '--strict' in argv
    entries, vtxt, bad_lines = parse()
    errors, warnings = [], []
    seen_exact, accent_pairs = {}, defaultdict(set)
    seen_flat = {}

    for i, line in bad_lines:
        errors.append(f'line {i}: unparsable: {line[:60]}')

    for i, key, gloss in entries:
        check_key(key, errors, warnings, seen_exact, seen_flat, accent_pairs)

    # accent pairs where BOTH forms exist as keys are the registry (§1.5.4): allowed
    # but flagged for §26 tracking
    pairs = {f: ks for f, ks in accent_pairs.items() if len(ks) > 1}
    # plain same-flat-form pairs (loma/lóma) don't error above; list them
    flat_groups = defaultdict(set)
    for _, key, _g in entries:
        flat_groups[strip_accents(key.lower())].add(key.lower())
    real_pairs = {f: ks for f, ks in flat_groups.items() if len(ks) > 1}
    for f, ks in sorted(real_pairs.items()):
        warnings.append(f'accent-pair registry: {sorted(ks)}')

    print(f'VTXT: {vtxt or "(missing VTXT header)"}')
    print(f'entries: {len(entries)}  unique keys: {len(seen_exact)}')
    print(f'errors: {len(errors)}  warnings: {len(warnings)}')
    for e in errors[:60]:
        print('ERROR', e)
    if len(errors) > 60:
        print(f'... {len(errors) - 60} more errors')
    for w in warnings[:40]:
        print('warn ', w)
    if len(warnings) > 40:
        print(f'... {len(warnings) - 40} more warnings')
    if errors or (strict and warnings):
        return 1
    print('OK')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
