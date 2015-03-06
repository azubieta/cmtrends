from twitter_api import api
from twitter_api.models import User
from twitter_api.models import Status



def measure_activity(name):
	pass

def list_followers():
	user = User.remote.fetch('CMobileTrends')
	followers = api.api_call('followers', user.id)
	return followers

def list_candidates():
	followers = list_followers()
	confirmed = list_friends()
	candidates = []
	for follower in followers:
		if not follower in confirmed:
			candidates.append(follower)
	
	return candidates
	
def list_friends():
	user = User.remote.fetch('CMobileTrends')
	followers = api.api_call('friends', user_id=user.id)
	return followers
	
def confirm_id(id):
	api.api_call('create_friendship', user_id=id)
	
def confirm_name(name):
	user = User.remote.fetch(name)
	confirm_id(user.id)

def discover_initiative_tweets(since_id):
	tweets = api.api_call('search', '#Initiative @CMobileTrends')
	return tweets
	

