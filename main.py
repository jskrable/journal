#!/usr/bin/env python3
# coding: utf-8
"""
title: main.py
date: 2019-08-23
author: jack skrable
description: a cmd line program built to prompt, record, and store journal entries
"""

import os
import getpass
import argparse
import datetime
import subprocess



# dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


def get_working_directory():
	if os.name == 'posix':
		cwd = '/home/{}/journal/'.format(getpass.getuser())
	else:
		cwd = 'C:/users/{}/journal/'.format(getpass.getuser())

	if not os.path.exists(cwd):
		os.mkdir(cwd)

	return cwd


def inline_input():
	print('Talk, brother...\n')
	return input('\n')

def get_entry(outfile):
	EDITOR = os.environ.get('EDITOR','vim') #that easy!
	initial_message = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') # if you want to set up the file somehow
	print('Talk, brother...\n')
	with open(outfile, 'w+') as f:
		f.write(initial_message)
		f.write('\n\n')
		f.flush()
		# f.seek(0,2)
		subprocess.call([EDITOR, f.name])


def prompt_user():
	entry = {
			'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
			'contents': inline_input()
			}
	return entry


def write_file(outfile,entry):
	with open(outfile, 'w+') as f:

		f.write(entry['date']+'\n\n')
		f.write(entry['contents']+'\n\n')


# MAIN
#############################################
dt = datetime.datetime.now().strftime('%Y%m%d%H%M')

# use vim
get_entry(get_working_directory()+'{}.txt'.format(dt))

# use input
# write_file(get_working_directory()+'{}.txt'.format(dt),prompt_user())