import facebook
import json


ACCESS_TOKEN= 'CAACEdEose0cBAAxzznKQRj5yRhwvSvvBKh5dVKOjspQzeJqhZCWcjFKVvOe7rrukGOKqoG72kABtBjEsWSlPPYybZCW0aeo2l1a6GEc5AUEyZBlUOXJlxZAPKVZBLboC8HqddUvb8rrNFqtorL2l9tpKwvr2QCmw2jlSeb1sDAGuq5ZB5ZB83aGbkJRTZAvnc7ebw7MCKp16D6VdZC07113Pr'

# simple function to pretty print some json objects
def pp(o):
  print json.dumps(o, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)

print '---------------'
print 'Me'
print '---------------'
pp(g.get_object('me'))

print
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections('me' , 'friends'))
