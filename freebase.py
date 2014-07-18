#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-07-17 16:18:04
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-07-18 09:16:19
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

import json
import urllib

def foo():
	api_key = 'AIzaSyCyOX5A9WqWEMdNKVJtWR6FB4T6Ru1n14I'

	query = 'beef stroganoff recipe'
	service_url = 'https://www.googleapis.com/freebase/v1/search'
	params = {
	        'query': query,
	        'key': api_key
	}
	url = service_url + '?' + urllib.urlencode(params)

	response = urllib.urlopen(url).read()

	with open('morel mushrooms.json','w') as f:
		f.write(response)

	response = json.loads(response)

	print response

	

	for result in response['result']:
	    print result['name'],result['score']




if __name__ == '__main__':
	foo()







	