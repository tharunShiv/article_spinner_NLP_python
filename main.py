# from __future__ import print_function, division
# from future.utils import iteritems
# from builtins import range

import nltk
# for the probability
import random
import numpy as np
# for iteritems
import six

from bs4 import BeautifulSoup

# load the reviews
# data courtesy of http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html
positive_reviews = BeautifulSoup(open('electronics/positive.review').read())
positive_reviews = positive_reviews.findAll('review_text')

# extract trigrams and insert into dictionary
# (w1, w3) is the key, [ w2 ] are the values
trigrams = {}
for review in positive_reviews:
    s = review.text.lower()
    '''
    example token: Tokens: ['the', 'gps', 'works', 'in', 'both', 'my', 'dell',
    'axim', 'x5', 'and', 'in', 'my', 'hp', 'compaq', 'nc6000', 'with', 'a', 'compact',
    'flash', 'adapter', 'card', '.', 'i', 'have', 'used', 'it', 'with', 'ms', 'streets', 'and', 'trips', 'and', 'arcpad']
    '''
    tokens = nltk.tokenize.word_tokenize(s)
    # print("Tokens: "+str(tokens))
    for i in range(len(tokens) - 2):
        # key
        # prev word and next word
        k = (tokens[i], tokens[i+2])
        if k not in trigrams:
            trigrams[k] = []
        trigrams[k].append(tokens[i+1])

# turn each array of middle-words into a probability vector
# trigram: ('message', 'the'): ['in']
# k: ('message', 'the')words: ['in']
#  ('while', 'with'): {'driving': 0.5, 'talking': 0.5},
trigram_probabilities = {}
for k, words in six.iteritems(trigrams):
    # create a dictionary of word -> count
    if len(set(words)) > 1:
        # only do this when there are different possibilities for a middle word
        d = {}
        n = 0
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
            n += 1
        for w, c in six.iteritems(d):
            d[w] = float(c) / n
        trigram_probabilities[k] = d


def random_sample(d):
    # choose a random sample from dictionary where values are the probabilities
    r = random.random()
    cumulative = 0
    for w, p in six.iteritems(d):
        cumulative += p
        if r < cumulative:
            return w

# picking a random review and spinning it
def test_spinner():
    review = random.choice(positive_reviews)
    s = review.text.lower()
    print("Original:", s)
    tokens = nltk.tokenize.word_tokenize(s)
    for i in range(len(tokens) - 2):
        if random.random() < 0.2: # 20% chance of replacement
            k = (tokens[i], tokens[i+2])
            if k in trigram_probabilities:
                w = random_sample(trigram_probabilities[k])
                tokens[i+1] = w
    print("Spun:")
    print(" ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))


if __name__ == '__main__':
    test_spinner()
