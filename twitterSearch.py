import twitter
import json
from prettytable import PrettyTable

from collections import Counter

CONSUMER_KEY = 'VyqTPV8n1OvdGYrz7aw03qci7'
CONSUMER_SECRET = '1aGLspKsVEmVaG7AvkITOzak99iMNUs41lE39Md1RBtNbxraHi'
OAUTH_TOKEN = '75975306-X2wUaGSodK8Gv4vhfaCjW9gsCjsel2OZKTFqAdZSg'
OAUTH_TOKEN_SECRET = 'ebS5e5PgqII2cKKFQsluW80GdhIN8YQZOkJmtClCVxTul'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = 'FIFA'
count = 100

search_results = twitter_api.search.tweets(q=q , count=count)
# print json.dumps(search_results , indent=1)

statuses = search_results['statuses']

for _ in range(5):
  try:
    next_results = search_results['search_metadata']['next_results']
  except KeyError, e:
    break

  kwargs = dict([ kv.split('=') for kv in
                 next_results[1:].split("&") ])

  search_results = twitter_api.search.tweets(**kwargs)
  statuses+= search_results['statuses']

# print json.dumps(statuses[1], indent=1)  #MIGHT NEED TO MODIFY to 0!!!!!!!

status_texts = [status['text'] for status in statuses]
screen_names = [user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]
hashtags = [ hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags'] ]

# computing all words here
words = [w for t in status_texts for w in t.split() ]
#
# print json.dumps(status_texts[0:5], indent=1)
# print json.dumps(screen_names[0:5], indent=1)
# print json.dumps(hashtags[0:5], indent=1)
# print json.dumps(words[0:5], indent=1)


for item in [words, screen_names, hashtags] :
  c = Counter(item)
  print c.most_common()[:10]
  print


for label,data in (('Hashtag' , hashtags) , ('Wooord' , words)):
  pt = PrettyTable(field_names = [label, 'Count'])
  c = Counter(data)
  [ pt.add_row(kv) for kv in c.most_common()[:10] ]
  pt.align[label], pt.align['Count'] = 'l', 'r'
  print pt
  #just done
  
























# end here
