import json
import requests
from requests_oauthlib import OAuth1

import secrets

client_key = secrets.TWITTER_API_KEY
client_secret = secrets.TWITTER_API_SECRET

access_token = secrets.TWITTER_ACCESS_TOKEN
access_token_secret = secrets.TWITTER_ACCESS_TOKEN_SECRET

oauth = OAuth1(client_key,
            client_secret=client_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret)

def construct_unique_key(baseurl, params):
    param_strings = []
    connector = '_'
    for k in params.keys():
        param_strings.append(f'{k}_{params[k]}')
    param_strings.sort()
    unique_key = baseurl + connector +  connector.join(param_strings)
    return unique_key

endpoint_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q': '@umsi'}
print(construct_unique_key(endpoint_url, params))

endpoint_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q': '@umsi', 'count':'100', 'foo': 'bar'}
print(construct_unique_key(endpoint_url, params))

endpoint_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'foo': 'bar', 'q': '@umsi', 'count':'100', }
print(construct_unique_key(endpoint_url, params))

response = requests.get(endpoint_url, params=params, auth=oauth)

results = response.json()
tweets = results['statuses']
for t in tweets:
    print(t['text'])

