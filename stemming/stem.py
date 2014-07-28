#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-07-28 23:10:10
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-07-28 23:24:33
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

from nltk.stem import PorterStemmer
import os
import re


def foo():
	root = './queries/'
	files = os.listdir(root)
	stemmer = PorterStemmer()
	puncre = re.compile(r'[^0-9a-zA-Z\']')

	for qf in files:
		qfp = root+qf
		with open(qfp) as f:
			content = f.read().split('\n')
		lines = []
		for line in content:
			ts = line.split(':',1)
			print ts
			number = ts[0]+' : '
			queries=puncre.split(ts[1])
			tql = [number]
			for query in queries:
				tql.append(query)
				sq = stemmer.stem(query)
				if sq != query:
					tql.append(sq)
			lines.append(' '.join(tql))
		qfp += '.stem.txt'
		with open(qfp,'w') as f:
			f.write('\n'.join(lines))




if __name__ == '__main__':
	# a = re.compile(r'[^a-zA-Z0-9\']')
	# print a.split('hello\'s world')
	foo()








	