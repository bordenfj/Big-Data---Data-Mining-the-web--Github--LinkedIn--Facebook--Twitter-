import requests
import json

base_url = 'https://graph.facebook.com/me'

fields = 'id,name,friends.limit(2).fields(likes.limit(2))'

ACCESS_TOKEN= 'CAACEdEose0cBAAxzznKQRj5yRhwvSvvBKh5dVKOjspQzeJqhZCWcjFKVvOe7rrukGOKqoG72kABtBjEsWSlPPYybZCW0aeo2l1a6GEc5AUEyZBlUOXJlxZAPKVZBLboC8HqddUvb8rrNFqtorL2l9tpKwvr2QCmw2jlSeb1sDAGuq5ZB5ZB83aGbkJRTZAvnc7ebw7MCKp16D6VdZC07113Pr'

url = '%s?fields=%s&access_token=%s' %  (base_url, fields, ACCESS_TOKEN)

# print url

content = requests.get(url).json()

print json.dumps(content , indent=1)
