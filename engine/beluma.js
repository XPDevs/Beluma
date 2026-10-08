/* ============================================================
   Beluma v3 — core language engine.
   Loads h.txt, builds both indices, and translates English <-> Beluma
   using real morphological rules (not word substitution).
   ============================================================ */
(function (global) {
  'use strict';

  const DICT_URL = global.BELUMA_DICT_URL || '../lexicon/h.txt';

  /* ---------- state ---------- */
  const enToBe = {};
  const beToEn = {};
  let dictVersion = '3.1';
  let dictReady = false;

  /* ---------- affixes ---------- */
  const SUFFIXES = [
    { aff: 'pira', en: 'tool for ', kind: 'nom' },
    { aff: 'sula', en: 'great ', kind: 'aug' },
    { aff: 'tavi', en: 'platform for ', kind: 'nom' },
    { aff: 'lek', en: 'place of ', kind: 'loc' },
    { aff: 'nira', en: 'small ', kind: 'dim' },
    { aff: 'la', en: "'s", kind: 'gen' },
    { aff: 'le', en: '-ly', kind: 'adv' },
    { aff: 'va', en: '-ing', kind: 'part' },
    { aff: 'ke', en: 'done (past participle) ', kind: 'part' },
    { aff: 'et', en: 'young ', kind: 'dim' },
    { aff: 'os', en: 'group of ', kind: 'col' },
    { aff: 'an', en: 'place of ', kind: 'loc' },
    { aff: 'or', en: 'one who does ', kind: 'agent' },
    { aff: 'ji', en: '-th', kind: 'ord' },
    { aff: 'ik', en: '-like ', kind: 'adj' },
    { aff: 'as', en: '', kind: 'pl' },
    { aff: 's', en: '', kind: 'pl' }
  ];
  const PREFIXES = [
    { aff: 'un', en: 'not ' },
    { aff: 'ni', en: 'opposite of ' },
    { aff: 're', en: 'again ' }
  ];

  /* ---------- helpers ---------- */
  function normalizeAccents(s) {
    return String(s).replace(/[áéíóú]/g, ch => ({ 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u' })[ch]);
  }
  const isVowel = c => 'aeiou'.includes(c);
  function pluralSuffixBE(root) { return isVowel(root[root.length - 1]) ? 's' : 'as'; }
  function pluralizeEN(w) {
    if (!w) return w;
    if (/[^aeiou]y$/.test(w)) return w.slice(0, -1) + 'ies';
    if (/(s|ss|sh|ch|x|z)$/.test(w)) return w + 'es';
    return w + 's';
  }
  const EN_PAST = {
    eat: 'ate', drink: 'drank', sleep: 'slept', go: 'went', run: 'ran', see: 'saw',
    know: 'knew', bring: 'brought', give: 'gave', take: 'took', make: 'made', do: 'did',
    say: 'said', hear: 'heard', sing: 'sang', swim: 'swam', fly: 'flew', win: 'won',
    can: 'could',
    understand: 'understood', tell: 'told', speak: 'spoke', feel: 'felt', build: 'built',
    cut: 'cut', sit: 'sat', stand: 'stood', write: 'wrote', buy: 'bought', sell: 'sold',
    grow: 'grew', live: 'lived', play: 'played', wait: 'waited', open: 'opened',
    close: 'closed', start: 'started', finish: 'finished', change: 'changed', send: 'sent',
    find: 'found', have: 'had', is: 'was', are: 'were', am: 'was', jump: 'jumped',
    love: 'loved', help: 'helped', want: 'wanted', live: 'lived', teach: 'taught',
    run: 'ran', get: 'got', think: 'thought', come: 'came', leave: 'left', read: 'read'
  };
  function pastEN(base) {
    const k = String(base).toLowerCase().split(' ')[0];
    if (EN_PAST[k]) return EN_PAST[k];
    if (/e$/.test(k)) return k + 'd';
    return k + 'ed';
  }
  function futureEN(base) { return 'will ' + String(base).toLowerCase().split(' ')[0]; }

  /* ---------- fixed English -> Beluma word layer ---------- */
  const FIXED_EN = {
    i: 'mi', me: 'mu', you: 'tu', he: 'nivo', him: 'nivo', she: 'siva', it: 'et',
    we: 'mis', us: 'mis', they: 'misu', them: 'misu', my: 'mi-la', your: 'tu-la',
    his: 'nivo-la', its: 'et-la', our: 'mis-la', their: 'misu-la',
    a: 'o', an: 'o', the: 'le', and: 'unas', or: 'ora', but: 'neka', than: 'ban',
    very: 'vevlo', not: 'un', no: 'non', yes: 'kek', by: 'li', at: 'na', in: 'na',
    to: 'po', from: 'de', for: 'fao', with: 'vel', on: 'su', under: 'un-su',
    who: 'kvasi', what: 'kwa', where: 'kwaras', when: 'kvado', why: 'kvaso', how: 'havi',
    which: 'kva', hello: 'sala', goodbye: 'ravi', thanks: 'nako', please: 'teva',
    sorry: 'noha', today: 'sofa', yesterday: 'safa', tomorrow: 'sova', day: 'diva',
    night: 'noita', week: 'soma', month: 'mava', year: 'suso', was: 'ne s', were: 'ne s',
    am: 's', is: 's', are: 's', be: 's', will: 'we', would: 'da-va', can: 'kima',
    could: 'da-va', may: 'nema', might: 'da-va', must: 'gida', should: 'sud',
    won: 'we un', cant: 'unkima', cannot: 'unkima', then: 'tola', that: 'ta',
    love: 'leva', one: 'ona', two: 'tuo', three: 'tro', four: 'fora',
    five: 'kvin', six: 'sixa', seven: 'sita', eight: 'oita', nine: 'noa', ten: 'diza',
    zero: 'zera', hundred: 'centa', thousand: 'mila', million: 'miliona',
    ate: 'ne fema', drank: 'ne neva', went: 'ne gai', ran: 'ne vira', saw: 'ne hena',
    knew: 'ne kema', brought: 'ne dova', gave: 'ne geva', took: 'ne losa', made: 'ne vesa',
    did: 'ne diva', said: 'ne sa', heard: 'ne sira', sang: 'ne niva', swam: 'ne niva',
    flew: 'ne hura', won: 'ne ziva', was: 'ne s', were: 'ne s', understood: 'ne kema',
    told: 'ne tela', spoke: 'ne sova', felt: 'ne tuma', built: 'ne vesa', sat: 'ne jesa',
    stood: 'ne misa', wrote: 'ne telora', bought: 'ne gava-pira', sold: 'ne gava-geva',
    grew: 'ne niva', lived: 'ne tita', played: 'ne sola', waited: 'ne sora', opened: 'ne dora',
    closed: 'ne tesa', started: 'ne jala', finished: 'ne vota', changed: 'ne tina',
    sent: 'ne nika', found: 'ne loma-pira', had: 'ne tova', left: 'ne lisa', loved: 'ne leva',
    helped: 'ne rava', wanted: 'ne nima', taught: 'ne miva', got: 'ne losa', came: 'ne gai',
    thought: 'ne kero-miva', read: 'ne dera', walked: 'ne vima', asked: 'ne pera',
    eats: 'fema', drinks: 'neva', sleeps: 'soma', goes: 'gai', runs: 'vira', flies: 'hura',
    sings: 'niva', sees: 'hena', knows: 'kema', says: 'sa', helps: 'rava', loves: 'leva',
    lives: 'tita', finds: 'loma-pira', plays: 'sola', opens: 'dora', wants: 'nima',
    reads: 'dera', writes: 'telora', speaks: 'sova', walks: 'vima', has: 'tova'
  };

  /* ---------- dictionary building ---------- */
  function buildIndices(fullText) {
    Object.keys(enToBe).forEach(k => delete enToBe[k]);
    Object.keys(beToEn).forEach(k => delete beToEn[k]);

    const lines = fullText.split(/\r?\n/);
    lines.forEach(line => {
      const t = line.trim();
      if (!t || t[0] === '#' || t.startsWith('---')) return;
      if (t.startsWith('VTXT=')) { dictVersion = t.slice(5).trim(); return; }
      const eq = t.indexOf('=');
      if (eq < 1) return;
      const beluma = normalizeAccents(t.slice(0, eq).trim().toLowerCase());
      const english = t.slice(eq + 1).trim();
      if (!beluma || !english) return;
      const primaryGloss = english.split('/')[0].trim();
      if (!beToEn[beluma]) {
        beToEn[beluma] = primaryGloss;
      } else if (beToEn[beluma].split(' / ').indexOf(primaryGloss) === -1) {
        // True homonymy: the same word surface has several dictionary senses
        // (e.g. "mila = thousand / my", "ra = near / was", "koro = bear / really?").
        // Keep every distinct sense so the translator can show the ambiguity,
        // exactly as a real dictionary lists homonyms together.
        beToEn[beluma] += ' / ' + primaryGloss;
      }
      english.split('/').forEach(g => {
        const key = g.toLowerCase().replace(/\s*\(.*?\)\s*/, '').trim();
        if (key && enToBe[key] === undefined) enToBe[key] = beluma;
      });
    });

    // Fixed function words (added only if the dictionary has none).
    Object.keys(FIXED_EN).forEach(k => { if (enToBe[k] === undefined) enToBe[k] = FIXED_EN[k]; });
    if (beToEn['beluma'] === undefined) beToEn['beluma'] = 'Beluma (the language)';
    dictReady = true;
  }

  async function loadDictionary(url) {
    url = url || DICT_URL;
    try {
      const res = await fetch(url + '?t=' + Date.now());
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const text = await res.text();
      buildIndices(text);
      return true;
    } catch (e) {
      if (url !== DICT_URL) return false;
      try { return await loadDictionary('https://xpdevs.github.io/Beluma/lexicon/h.txt'); }
      catch (e2) { return false; }
    }
  }

  /* ---------- Beluma word analysis (morphology strip + compound parsing) ---------- */

  let compoundDepth = 0;
  // resolveRoot: does THIS string name a real word, seen as a whole — a dictionary
  // root, or a head-first compound of resolvable roots (like nela + sula = ocean)?
  // Returns { root, gloss, parts:[{part, meaning}] } or null. Unlisted compounds are
  // accepted the same way the dictionary lists them, so speakers can coin new words.
  function resolveRoot(expr) {
    if (++compoundDepth > 8) { compoundDepth--; return null; }
    try {
      if (beToEn[expr]) return { root: expr, gloss: beToEn[expr], parts: [{ part: expr, meaning: beToEn[expr] }] };
      const segs = String(expr).split('-');
      if (segs.length > 1) {
        let plural = false;
        const lastIdx = segs.length - 1;
        if ((segs[lastIdx] === 's' || segs[lastIdx] === 'as') && segs.length > 2) {
          segs.pop(); plural = true;
        }
        const parts = [];
        for (const sg of segs) {
          if (!sg) return null;
          let r = resolveRoot(sg);
          if (!r && sg.endsWith('s')) { const st = sg.slice(0, -1); r = resolveRoot(st); if (r) { r.parts[r.parts.length - 1].part += 's'; r.parts[r.parts.length - 1].meaning += ' (pl)'; } }
          if (!r && sg.endsWith('as')) { const st = sg.slice(0, -2); r = resolveRoot(st); if (r) { r.parts[r.parts.length - 1].part += 's'; r.parts[r.parts.length - 1].meaning += ' (pl)'; } }
          if (!r) return null;
          // A part that is itself a homonym (e.g. siva = she / voice) offers its
          // first sense here, so a compound comes out "work-voice", not
          // "work-she / voice". The full homonym list stays in the analysis panel.
          r.parts.forEach(p => { p.meaning = String(p.meaning).split(' / ')[0].trim(); });
          parts.push(...r.parts);
        }
        if (plural && parts.length) {
          const p = parts[parts.length - 1];
          p.part += 's';
          p.meaning += ' (pl)';
        }
        const gloss = parts.map(p => p.meaning).join('-');
        return { root: expr, gloss, parts };
      }
      return null;
    } finally { compoundDepth--; }
  }

  function analyzeBeluma(word) {
    const w = normalizeAccents(String(word).toLowerCase().trim());
    if (!w) return null;
    const exact = beToEn[w];
    if (exact) return { word: w, gloss: exact, root: w, prefix: '', suffixes: [], parts: [{ part: w, meaning: exact }], known: true };

    let rest = w, prefix = '';
    for (const p of PREFIXES) {
      if (rest.startsWith(p.aff) && rest.length > p.aff.length && (beToEn[rest.slice(p.aff.length)] || resolveRoot(rest.slice(p.aff.length)))) {
        prefix = p.aff; rest = rest.slice(p.aff.length); break;
      }
    }
    const suffixes = [];
    // Only strip an affix when it reveals a real dictionary word — unlisted
    // compound forms ("luma-pira", "siva-nela") are kept whole and resolved
    // as head-first compounds instead. This mirrors how a lexicographic
    // dictionary is consulted and avoids false "nena-v" splits.
    while (rest.length > 1 && suffixes.length < 4 && !beToEn[rest]) {
      const before = rest;
      for (const sfx of SUFFIXES) {
        const aff = sfx.aff;
        if (rest.length <= aff.length + 1 || !rest.endsWith(aff)) continue;
        // hyphen-aware slicing: "fema-pira-s" -> stem "fema-pira", not "fema-pira-"
        let cut = rest.length - aff.length;
        if (rest[cut - 1] === '-') cut -= 1;
        const stem = rest.slice(0, cut);
        if (stem && beToEn[stem]) { rest = stem; suffixes.push(sfx); break; }
      }
      if (rest === before) break;
    }
    const base = resolveRoot(rest);
    if (base) {
      const gloss = (prefix ? (PREFIXES.find(p => p.aff === prefix).en || '').replace(/\s*\(.*?\)\s*/g, '').trim() + ' ' : '') + base.gloss;
      let parts = prefix ? [{ part: prefix + '-', meaning: (PREFIXES.find(p => p.aff === prefix).en || 'not ').trim() }] : [];
      parts = parts.concat(base.parts);
      suffixes.forEach(s => parts.push({ part: '-' + s.aff, meaning: (s.en || '') + (s.kind === 'pl' ? ' (plural)' : '') }));
      return { word: w, gloss, root: rest, prefix, suffixes, parts, known: false };
    }
    return null;
  }

  function describeAnalysis(a) {
    if (!a) return { summary: '', table: [] };
    if (a.known) return { summary: a.gloss, table: [{ part: a.word, meaning: a.gloss }] };
    const rows = (a.parts || []).slice();
    const summary = (a.parts || []).map(p => p.meaning).join(' ');
    return { summary: a.gloss, table: rows.length ? rows : [{ part: a.root, meaning: a.gloss }] };
  }

  /* ---------- tokenizing ---------- */
  function tokenize(text) {
    return text.split(/([ \t\n\r\f\v]|[.,!?;:'"()])/).filter(t => t && t.length > 0);
  }

  /* ---------- English -> Beluma ---------- */
  function enRootFromInflected(enWord) {
    const lower = enWord.toLowerCase();
    const found = [], add = (root, infl) => { if (enToBe[root]) found.push({ root, infl }); };
    add(lower, 'plain');
    if (/^[a-z]+'s$/.test(lower)) add(lower.replace(/'s$/, ''), 'gen');
    if (/(ies)$/.test(lower)) add(lower.replace(/ies$/, 'y'), 'plural');
    if (/(es)$/.test(lower)) add(lower.replace(/es$/, ''), 'plural');
    if (/(s)$/.test(lower)) add(lower.replace(/s$/, ''), 'plural');
    if (/(ing)$/.test(lower)) {
      const stem = lower.replace(/ing$/, '');
      add(stem, 'ing'); add(stem.replace(/e$/, ''), 'ing');
    }
    if (/(ed)$/.test(lower)) {
      const stem = lower.replace(/ed$/, '');
      add(stem, 'past'); add(stem.replace(/e$/, ''), 'past');
    }
    if (/(d)$/.test(lower)) add(lower.replace(/d$/, ''), 'past');
    if (/(ly)$/.test(lower)) {
      const a = lower.replace(/ly$/, '');
      add(a, 'adv'); add(a.replace(/le$/, ''), 'adv');
    }
    if (/(er)$/.test(lower)) add(lower.replace(/er$/, ''), 'comparative');
    if (/(est)$/.test(lower)) add(lower.replace(/est$/, ''), 'superlative');
    if (/(es)$/.test(lower)) add(lower.replace(/es$/, ''), 'plural');
    return found[0] || null;
  }

  function enToBeToken(token) {
    const lower = token.toLowerCase();
    // Beluma function words pass through when typed in a mixed sentence
    const BE_PASSTHROUGH = { du: 1, kvo: 1, kek: 1, non: 1, sala: 1, ravi: 1, nako: 1, teva: 1,
      un: 1, ne: 1, we: 1, s: 1, le: 1, o: 1, ta: 1, kva: 1, kvasi: 1, kwaras: 1, kvado: 1, kvaso: 1, havi: 1 };
    if (BE_PASSTHROUGH[lower]) return { text: lower, unknown: false };
    // English hyphen compounds ("water-fruit", "light-tool") translate head-first
    if (lower.includes('-')) {
      const segs = lower.split('-').filter(Boolean);
      if (segs.length > 1) {
        const parts = segs.map(s => {
          const h = enRootFromInflected(s);
          return enToBe[(h && h.root) || s];
        });
        if (parts.every(Boolean)) return { text: parts.join('-'), unknown: false };
      }
    }
    const hit = enRootFromInflected(lower);
    if (!hit) return { text: token, unknown: true };
    const beluma = (enToBe[hit.root] || '').trim();
    switch (hit.infl) {
      case 'gen': return { text: beluma + '-la', unknown: false };
      case 'plural': return { text: beluma + pluralSuffixBE(beluma), unknown: false };
      case 'ing': return { text: beluma + '-va', unknown: false };
      case 'past': return { text: 'ne ' + beluma, unknown: false };
      case 'adv': return { text: beluma + '-le', unknown: false };
      case 'comparative': return { text: 'mesa ' + beluma, unknown: false };
      case 'superlative': return { text: 'susa ' + beluma, unknown: false };
      default: return { text: beluma, unknown: false };
    }
  }

  /* ---------- Beluma -> English ---------- */
  const TENSE_MARKERS = { 'ne': 'PAST', 'we': 'FUT', 'wes': 'IMM' };
  const VERB_ROOTS = new Set([
    'gai','fema','neva','hena','kema','sova','tela','dova','geva','losa','vasa',
    'vesa','fera','tora','jiva','jesa','niva','vira','hura','roma','mora','kisa',
    'lisa','tita','ziva','leva','nima','soma','diva','sira','loma','sola','dera',
    'tuna','puma','zura','rala','gava','pavra','rola','nikas','tina','vota','jala',
    'lora','zanva','fola','pera','sak','triva','kosa','tusa','ruana',
    'tita','dasa','davo','lida','sova','tusa','rova','rava','soma','esto'
  ]);

  function beToEnToken(token) {
    const lower = token.toLowerCase();
    const analysis = analyzeBeluma(lower);
    if (!analysis) return { text: token, root: lower, unknown: true };

    if (TENSE_MARKERS[normalizeAccents(lower)]) return { text: '', root: lower, tense: TENSE_MARKERS[normalizeAccents(lower)], unknown: false };
    if (lower === 'kvo') return { text: 'Do', root: lower, qmark: true, unknown: false };
    if (lower === 'du') return { text: '', root: lower, negImp: true, unknown: false };
    if (lower === 'un') return { text: '', root: lower, neg: true, unknown: false };

    let gloss = analysis.gloss;
    if (analysis.known) gloss = analysis.gloss.split(' / ')[0].trim();
    if (!analysis.known) {
      const rootGloss = analysis.gloss || '';
      const parts = [];
      if (analysis.prefix) {
        const p = PREFIXES.find(x => x.aff === analysis.prefix);
        parts.push(p.en.trim() + rootGloss);
      } else {
        parts.push(rootGloss);
      }
      analysis.suffixes.forEach(s => {
        if (s.kind === 'pl') { parts.push(s.en.trim() || ''); }
        else parts.push(s.en.trim());
      });
      // rebuild: qualifiers (adjectives, "tool for", "young", …) come BEFORE
      // the head noun, the way English orders modifiers: "small bird", not
      // "bird small". Plural handled after.
      let base = parts[0] || rootGloss;
      const extras = parts.slice(1).filter(x => x);
      if (extras.length) base = extras.join(' ') + ' ' + base;
      // drop an empty prefix that produced a double space
      base = base.replace(/\s+/g, ' ').trim();
      gloss = base;
      // simplify plural rendering
      if (analysis.suffixes.some(s => s.kind === 'pl')) {
        const first = analysis.gloss.split(' ')[0];
        if (analysis.suffixes.some(s => s.kind !== 'pl')) {
          gloss = gloss + ' (plural)';
        } else {
          gloss = pluralizeEN(analysis.gloss);
        }
      }
    }
    return { text: gloss, root: analysis.root, unknown: false };
  }

  function applyTenseToWord(analysisResult, tense) {
    if (!tense || analysisResult.unknown) return analysisResult.text;
    let w = analysisResult.text;
    if (tense === 'PAST') {
      const first = w.split(' ')[0];
      if (EN_PAST[first] || /ed$/.test(first)) return pastEN(first) + w.slice(first.length);
      return pastEN(first) + w.slice(first.length);
    }
    if (tense === 'FUT') return futureEN(w);
    if (tense === 'FUT-NEG') return 'will not ' + w.split(' ')[0];
    if (tense === 'NEG-FUT') return 'will not ' + w.split(' ')[0];
    if (tense === 'NEG-PAST') return 'did not ' + w.split(' ')[0];
    return w;
  }

  function translateEnToBe(text) {
    // Question auxiliaries: "Do you go?" -> kvo + pronoun; imperative "do not"/"don't" -> du
    let src = text
      .replace(/\b(do|does|did)\s+(you|we|they|he|she|it)\b/gi, 'kvo $2')
      .replace(/\b(do|does|did)\s+not\b/gi, 'du')
      .replace(/\bd[o']?nt\b/gi, 'du');
    const out = [];
    tokenize(src).forEach(tok => {
      if (/^\s+$/.test(tok) || /^[.,!?;:'"()]$/.test(tok)) { out.push({ text: tok, unknown: false, raw: tok }); return; }
      const r = enToBeToken(tok);
      out.push({ text: r.text, unknown: r.unknown, raw: tok });
    });
    // capitalize first letter of output for the first non-punct token
    let capDone = false, capState = 1;
    for (let i = 0; i < out.length; i++) {
      const p = out[i].text;
      if (!p || /^\s+$/.test(p)) continue;
      if (/^[.,!?;:()]$/.test(p)) continue;
      if (!capDone) {
        out[i].text = p.charAt(0).toUpperCase() + p.slice(1);
        capDone = true;
      }
    }
    return out;
  }

  function translateBeToEn(text) {
    text = normalizeAccents(text);
    // Whole-phrase (collocation / idiom) lookup first: multi-word dictionary
    // entries such as "mila nésa = my house" and "sala mi-la = hello my friend"
    // match as chunks before word-by-word parsing, like a real idiom dictionary.
    const wholeKey = text.toLowerCase().trim().replace(/[?!.,;:’'"()]+$/, '');
    const collocGloss = beToEn[wholeKey];
    if (collocGloss) return [{ text: collocGloss.charAt(0).toUpperCase() + collocGloss.slice(1), unknown: false, raw: wholeKey }];
    const out = [];
    let pendingTense = '';
    let pendingQ = false;
    let pendingImp = false;
    let capDone = false;
    let lastRoot = '';
    let lastRaw = '';
    // idiomatic "how are you / he / she ..." => reorder to English
    const howMap = { mi: 'I', tu: 'you', nivo: 'he', siva: 'she', et: 'it', mis: 'we', tur: 'you', misu: 'they' };
    text = text.replace(/\bhavi\s+(mi|tu|nivo|siva|et|mis|tur|misu)\s+s\b/gi, (m, g) => 'havi are ' + howMap[g.toLowerCase()]);
    tokenize(text).forEach((tok, i, arr) => {
      if (/^\s+$/.test(tok) || /^[.,!?;:'"()]$/.test(tok)) { out.push({ text: tok, unknown: false, raw: tok }); return; }
      const r = beToEnToken(tok);
      if (r.tense) { pendingTense = pendingTense === 'NEG' ? 'NEG-' + r.tense : r.tense; out.push({ text: '', unknown: false, raw: tok }); return; }
      if (r.qmark) { pendingQ = true; if (!capDone) { out.push({ text: 'Do', unknown: false, raw: tok }); capDone = true; } else { out.push({ text: 'do', unknown: false, raw: tok }); } return; }
      if (r.negImp) { pendingImp = true; out.push({ text: '', unknown: false, raw: tok }); return; }
      if (r.neg) { pendingTense = 'NEG'; out.push({ text: '', unknown: false, raw: tok }); return; }
      let t = r.text || '';
      // koro is a homonym (bear / discourse marker). The "really?" reading is
      // cued by a following question mark; elsewhere the animal sense stands.
      const nextTok = () => { for (let j = i + 1; j < arr.length; j++) if (!/^\s+$/.test(arr[j])) return arr[j]; return ''; };
      if (normalizeAccents(tok.toLowerCase().trim()) === 'koro' && /^\?/.test(nextTok())) t = "Really"; // the following '?' token adds the mark
      if (t === 'is' && r.root === 's') {
        t = ({ mi: 'am', mu: 'am', tu: 'are', nivo: 'is', siva: 'is', ét: 'is', et: 'is', mis: 'are', tur: 'are', misu: 'are' }[lastRoot]) ||
            (/s$/.test(lastRoot) || /s$/.test(lastRaw) ? 'are' : 'is');
      }
      let doNot = false;
      if (pendingImp) {
        t = "Don't " + (t || ''); pendingImp = false;
      } else if (pendingTense === 'NEG') {
        if (r.root === 'esto') { t = 'There is no'; pendingTense = ''; }
        else { const isVerb = VERB_ROOTS.has(r.root); t = prefixNeg(t, isVerb); pendingTense = ''; }
      } else if (pendingTense && t) {
        if (pendingTense === 'IMM') {
          // "about to": subject conjugation only (the subject word already printed)
          const subj = { mi: 'am ', tu: 'are ', nivo: 'is ', siva: 'is ', et: 'is ',
            mis: 'are ', tur: 'are ', misu: 'are ', miro: 'are ', zava: 'is ' };
          t = (subj[lastRoot] || 'is ') + 'about to ' + t;
        } else {
          t = applyTenseToWord(r, pendingTense);
        }
        pendingTense = '';
        if (t.startsWith('will') && t === 'will not ') pendingTense = '';
      }
      if (r.root) { lastRoot = r.root; lastRaw = tok; }
      if (t && !capDone) { t = t.charAt(0).toUpperCase() + t.slice(1); capDone = true; }
      out.push({ text: t, unknown: r.unknown, raw: tok });
    });
    if (pendingQ) {
      // ensure closing question mark
      let last = out[out.length - 1];
      if (last && last.text && !/[?]$/.test(last.text)) out.push({ text: '?', unknown: false, raw: '?' });
    }
    return out;
  }

  function analysisRoot(gloss) {
    if (!gloss) return '';
    const low = gloss.toLowerCase();
    if (beToEn[low]) return low;
    return low.split(' ')[0];
  }

  function prefixNeg(t, isVerb) {
    if (!t) return t;
    const first = t.toLowerCase().split(' ')[0];
    if (isVerb) {
      // do not / does not / did not depending on tense left by earlier marker
      return "do not " + t.charAt(0).toLowerCase() + t.slice(1);
    }
    return "not " + t.charAt(0).toLowerCase() + t.slice(1);
  }

  function pcase(s) {
    if (!s) return s;
    if (s === s.toUpperCase() && s.length > 1) s = s.toLowerCase();
    return s.charAt(0).toUpperCase() + s.slice(1);
  }

  /* ---------- public API ---------- */
  global.Beluma = {
    loadDictionary,
    buildIndices,
    dictReady: () => dictReady,
    dictVersion: () => dictVersion,
    countBe: () => Object.keys(beToEn).length,
    analyzeBeluma,
    describeAnalysis,
    translateEnToBe,
    translateBeToEn,
    enToBe,
    beToEn
  };
})(typeof globalThis !== 'undefined' ? globalThis : window);