import secret_keys
import tweepy
from joke_writing_machine import get_joke

api_key = secret_keys.twitter_api_key
api_key_secret = secret_keys.twitter_api_key_secret
access_token = secret_keys.twitter_access_token
access_token_secret = secret_keys.twitter_access_token_secret

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator)

api.update_status(get_joke())