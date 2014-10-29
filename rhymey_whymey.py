import argparse
import json
import random
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='min_syllables', type=int, help='minimum syllable count', default=2)
    parser.add_argument('-M', dest='max_syllables', type=int, help='maximum syllable count', default=3)
    parser.add_argument('-w', dest='words', type=int, help='word count', default=2)
    parser.add_argument('-i', dest='iterations', type=int, help='iterations', default=3)
    args = parser.parse_args()

    with open('rhyming_dict.json', 'r') as fp:
        common_words = json.load(fp)

    eligible_d = {}
    for syllable_length in xrange(args.min_syllables, args.max_syllables + 1):
        for (k,v) in common_words[str(syllable_length)].iteritems():
            eligible_d[k] = eligible_d.get(k, []) + v

    eligible_d = {k: v for (k,v) in eligible_d.iteritems() if len(v) >= args.words}

    for iteration in xrange(args.iterations):
        print(' '.join(random.sample(random.choice(eligible_d.values()), args.words)))

if __name__ == '__main__':
    main()
