from itertools import dropwhile
import argparse
import random
import sys

from nltk.corpus import cmudict, words

def rhymes(f_word, s_word):
    # check that the stress (from the end) is the same
    return list(dropwhile(lambda s: '1' not in s, f_word)) == list(dropwhile(lambda s: '1' not in s, s_word))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='min_syllables', type=int, help='minimum syllable count', default=2)
    parser.add_argument('-M', dest='max_syllables', type=int, help='maximum syllable count', default=3)
    parser.add_argument('-w', dest='words', type=int, help='word count', default=2)
    parser.add_argument('-i', dest='iterations', type=int, help='iterations', default=3)
    args = parser.parse_args()

    d = cmudict.dict()
    w = words.words()
    d = dict((k, d[k]) for k in w if k in d)
    syllable_range = xrange(args.min_syllables, args.max_syllables + 1)
    eligible_d = dict((k, v[0]) for (k, v) in d.iteritems() if len([s for s in v[0] if s[-1].isdigit()]) in syllable_range)

    for iteration in xrange(args.iterations):
        successful_rhyme = False
        while not successful_rhyme:
        # pick a word!
            nwords = [random.choice(eligible_d.items())]
            rhyming_words = [(k, v) for (k, v) in eligible_d.iteritems() if (k != nwords[0][0] and rhymes(nwords[0][1], v))]
            try:
                nwords += random.sample(rhyming_words, args.words - 1)
            except ValueError:
                continue
            successful_rhyme = True
        print(' '.join(k for (k,__) in nwords))

if __name__ == '__main__':
    main()
