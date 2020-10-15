#!/usr/bin/env python3
# coding: utf-8
"""
title: analysis.py
date: 2020-10-06
author: jack skrable
description: sentiment analysis of journal entries
"""

import re
import os
import nltk
import numpy as np


def get_files(path='./journal'):
	"""
	Using input parameter of path, gathers a list of journal entry text files in
	a directory. Returns a list containing the absolute path of all files in provided
	directory. Default
	"""
	basedir = os.path.abspath(path)
	files = [os.path.join(basedir, file) for file in os.listdir(basedir)]
	return files

def read_file(file):
	"""
	Takes in a file path. Reads the file and parses the datetime from the filename. 
	Returns a dictionary with the datetime as key and file contents as value.
	"""
	date = file.split('/')[-1].split('.')[0]
	with open(file) as f:
		raw = f.read()
	return {date: raw}


def prep_entry(raw):
	"""
	Takes in a string containing a journal entry. Tokenizes the words, removes extraneous
	characters, and returns a list of individual words.
	"""
	# extra processing to remove non-standard characters and punctuation. necessary?
	words = [re.sub(r'[\W_]+', '', w).lower() for w in nltk.tokenize.word_tokenize(raw)]
	# words = nltk.tokenize.word_tokenize(raw)
	return words


def gather_entries(files):
	"""
	Using list of journal entry filepaths as input, reads the content of the files and
	creates a dictionary with the datetime of the entry as key and the contents as value.
	"""
	data = {}
	for f in files:
		data.update(read_file(f))
	return data


def create_corpus(data, method=''):
	"""
	use np?

	"""
	if method == 'np':
		words = np.array([np.array(prep_entry(raw)) for raw in data.values()])
		flat = np.concatenate(np_words)
	else:
		words = [prep_entry(raw) for raw in data.values()]
		flat = [item for sublist in words for item in sublist]

	stopwords = nltk.corpus.stopwords.words('english')
	stopwords.append('nt')
	corpus = [w for w in flat if w not in stopwords and w != '']
	return corpus



def create_dictionary(corpus):
	"""
	Not really sure what I'm doing here yet. Playing around with a dictionary and 
	NLTK features.
	"""
	# unique, counts = np.unique(np.array(corpus), return_counts=True)
	# dictionary = {w:counts[i] for i,w in enumerate(unique)}
	# sort = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

	# dictionary = [(i, corpus.count(i)) for i in set(corpus)]
	# dict_sort = sorted(dictionary, key=lambda x: x[1], reverse=True)


	frequency = nltk.FreqDist(corpus)
	print('Your top 15 words are:{}'.format(frequency.most_common()[:15]))
	f_long = set(sorted(w for w in corpus if len(w) > 7 and frequency[w] > 3))   
	print('Frequently used long words include:{}'.format(f_long))



def master():
	"""
	"""
	data = gather_entries(get_files())
	corpus = create_corpus(data)


"""
think about returning only latin chars?

consider punctuation?

ord("character") returns unicode char number

char(number) returns unicod char for number

try bigrams, trigrams
"""

