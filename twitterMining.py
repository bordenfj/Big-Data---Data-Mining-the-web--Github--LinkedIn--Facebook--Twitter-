import twitter

CONSUMER_KEY = 'VyqTPV8n1OvdGYrz7aw03qci7'
CONSUMER_SECRET = '1aGLspKsVEmVaG7AvkITOzak99iMNUs41lE39Md1RBtNbxraHi'
OAUTH_TOKEN = '75975306-X2wUaGSodK8Gv4vhfaCjW9gsCjsel2OZKTFqAdZSg'
OAUTH_TOKEN_SECRET = 'ebS5e5PgqII2cKKFQsluW80GdhIN8YQZOkJmtClCVxTul'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print twitter_api
