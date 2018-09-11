#!/usr/bin/python
import requests
import sys
import pocket_key

url = sys.argv[1]
consumer_key = pocket_key.consumer_key
access_token = '125a4db7-f3f4-3896-aa5c-5dd5a5'

requests.post('https://getpocket.com/v3/add', {'url': url, 'consumer_key': consumer_key, 'access_token': access_token})

