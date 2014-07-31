import twitter
import json

CONSUMER_KEY = 'VyqTPV8n1OvdGYrz7aw03qci7'
CONSUMER_SECRET = '1aGLspKsVEmVaG7AvkITOzak99iMNUs41lE39Md1RBtNbxraHi'
OAUTH_TOKEN = '75975306-X2wUaGSodK8Gv4vhfaCjW9gsCjsel2OZKTFqAdZSg'
OAUTH_TOKEN_SECRET = 'ebS5e5PgqII2cKKFQsluW80GdhIN8YQZOkJmtClCVxTul'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#trending topics

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id = WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id = US_WOE_ID)

# print json.dumps(world_trends , indent=1)

world_trends_set = set([trend['name']
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                     for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)
print common_trends
