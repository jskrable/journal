#!/usr/bin/env python3
# coding: utf-8
"""
title: analysis.py
date: 2020-10-06
author: jack skrable
description: sentiment analysis of journal entries
"""

import os
import numpy as np


def get_files(path='~/journal'):
	basedir = os.path.abspath(path)
	files = [os.path.join(basedir, file) for file in os.listdir(basedir)]

def read_file(file):
	"""
	"""
	date = file.split('/')[-1].split('.')[0]
	with open(file) as f:
		raw = f.read()
	return {date: raw}


def prep_entry(raw):
	words = [re.sub(r'[\W_]+', '', word).lower() for word in raw.split(' ').split('/')]
	return words


def gather_entries(files):
	"""
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
		np_words = np.array([np.array(prep_entry(raw)) for raw in data.values()])
		np_flat = np.concatenate(np_words)
		return np_flat
	else:
		words = [prep_entry(raw) for raw in data.values()]
		flat = [item for sublist in words for item in sublist]
		return flat


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
"""

