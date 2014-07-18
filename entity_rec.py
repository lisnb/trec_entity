#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-07-18 10:57:11
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-07-18 21:19:01
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""
import json
import urllib


def pureit():
	with open('web2014.topics.txt') as f:
		lines = f.readlines()
	lines = [x[4:] for x in lines]
	with open('web2014.topics.txt.pure','w') as f:
		f.write(''.join(lines))

def getalljson():
	with open('.api_key') as f:
		api_key = f.read()
	with open('web2014.topics.txt.pure') as f:
		topics = f.read().split('\n')

	service_url = 'https://www.googleapis.com/freebase/v1/search'

	a_tokens=[]

	logs = []

	params={
		'query':'query',
		'key':api_key
	}

	for topic in topics:
		try:
			tokens = topic.split()
			tlen = len(tokens)
			for i in range(0,tlen):
				for j in range(i+1,tlen+1):
					c_token = ' '.join(tokens[i:j])
					params['query']='\"%s\"'%c_token
					url = service_url + '?' + urllib.urlencode(params)
					# print url
					response = urllib.urlopen(url).read()
					# print response
					f_name = './jsons/%s.json'%c_token
					with open(f_name,'w') as f:
						f.write(response)
					response = json.loads(response)
					status = '%s\t%s'%(response['status'],c_token)
					print status
					logs.append(status)

		except Exception, e:
			print e 
		

	with open('freebase.log','w') as f:
		f.write('\n'.join(logs))


if __name__ == '__main__':
	# pureit()
	getalljson()







	