from itertools import dropwhile
import json

from nltk.corpus import cmudict, words

d = cmudict.dict()
w = words.words()

# first, get only the common words from cmudict
common_words = {k: d[k] for k in w if k in d}
rhyming_dict = {}
for word, prons in common_words.iteritems():
    for pron in prons:
        syllables = len(filter(lambda s: s[-1].isdigit(), pron))
        rhyme = '-'.join(dropwhile(lambda s: '1' not in s, pron)) if syllables > 1 else '-'.join(pron)
        try:
            rhyming_dict[syllables][rhyme].append(word)
        except KeyError:
            try:
                rhyming_dict[syllables][rhyme] = [word]
            except KeyError:
                rhyming_dict[syllables] = {rhyme: [word]}

with open('rhyming_dict.json', 'w') as fp:
    json.dump(rhyming_dict, fp)
