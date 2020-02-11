import json
from requests_oauthlib import OAuth1Session
import secrets

client_key = secrets.TWITTER_API_KEY
client_secret = secrets.TWITTER_API_SECRET

resource_owner_key = secrets.TWITTER_ACCESS_TOKEN
resource_owner_secret = secrets.TWITTER_ACCESS_TOKEN_SECRET


oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
results = r.json()
#print(json.dumps(results, indent=2))

tweets = results['statuses']
for t in tweets:
    print(t['text'])

