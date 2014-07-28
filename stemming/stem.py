#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-07-28 23:10:10
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-07-28 23:44:54
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

from nltk.stem import PorterStemmer
from stemming import porter2
import os
import re


def foo():
	root = './queries/'
	files = os.listdir(root)
	stemmer = PorterStemmer()
	puncre = re.compile(r'[^0-9a-zA-Z\']')

	# files = ['14.txt']

	words = set()

	for qf in files:
		qfp = root+qf
		with open(qfp) as f:
			content = f.read().split('\n')
		lines = []
		for line in content:
			# print line
			ts = line.split(':',1)
			# print ts
			number = ts[0]+':'
			queries=puncre.split(ts[1])
			tql = [number]
			for query in queries:
				tql.append(query)
				sq = stemmer.stem(query)
				# sq = porter2.stem(query)
				words.add(query)
				words.add(sq)
				# if sq != query:
					# tql.append(sq)
			lines.append(' '.join(tql))
		# qfp += '.stem_stemming.txt'
		# with open(qfp,'w') as f:
		# 	f.write('\n'.join(lines))


	qfp = 'words_nltk.txt'
	with open(qfp,'w') as f:
		f.write(' '.join(list(words)))




if __name__ == '__main__':
	# a = re.compile(r'[^a-zA-Z0-9\']')
	# print a.split('hello\'s world')
	# with open('./queries/14.txt') as f:
	# 	c = f.read()

	# with open('./queries/14.txt','w') as f:
	# 	f.write('\n'.join(c.split('\n\n')))
	foo()








	