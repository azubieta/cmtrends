from twitter_api import api
from twitter_api.models import User
from twitter_api.models import Status

def discover_tweets(since_id):
	tweets = api.api_call('search', '#Initiative @CMobileTrends', since_id = since_id)
	return tweets

