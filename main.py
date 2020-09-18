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


basedir = '/home/jskrable/journal'
dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


