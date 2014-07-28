import twitter

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

world_trend = twitter_api.trends.place(_id=WORLD_WOE_ID)
# us_trends = twitter_api.trends.place(_id=US_WOE_ID)

# print world_trend
# print
# print us_trends

tweets = twitter_api.search.tweets( q= 'helo')
print tweets
