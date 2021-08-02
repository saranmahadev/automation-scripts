import tweepy
import json
from quotes import get_quote

with open('keys.json') as json_data_file:
    data = json.load(json_data_file)

auth = tweepy.OAuthHandler(data["api-key"], data["api-secret"])
auth.set_access_token(data["access-token"], data["access-token-secret"])

api = tweepy.API(auth)

quote = get_quote()

api.update_status(status = quote[0]+"\n - "+quote[1])