# -*- coding: utf-8 -*-
from collections import Counter
import re

__author__ = 'goran'

sentence = 'I am Goran Iliev. I am cool.'

def get_words(text):
    return [w for w in re.split('\W+', text) if w]

def get_counts(words):
    return Counter(words)

words = get_words(sentence)

print(get_counts(words))

def get_tuples_count(words, model_num):
    N = len(words)
    counts = dict()
    for i in range(model_num, N):
        t = tuple(words[i - model_num:i])
        counts[t] = counts.get(t, 0) + 1
    return counts

def model_data(words, model_num=3):
    numerators = get_tuples_count(words, model_num)
    model_num -= 1
    denumerators = get_tuples_count(words, model_num)

    return numerators, denumerators

def get_likelihood(model_data, upcoming_word, previous_sequence):
    previous_tuple = tuple(previous_sequence)
    full_tuple = tuple(previous_sequence + [upcoming_word])

    full_tuples, previous_tuples = model_data

    return 1.0 * full_tuples[full_tuple] / previous_tuples[previous_tuple]


model_data = model_data(words)
print(get_likelihood(model_data, 'Goran', ['I', 'am']))
