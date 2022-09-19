import tweepy
import config
import json
from flask import Flask,request
import requests
app = Flask(__name__)

@app.route("/get",methods=["POST","GET"])
def retrieve_tweets():
    client = tweepy.Client(bearer_token=config.bearer_token)
    query = request.get_json()['query']
    tweet = client.search_recent_tweets(query = query,max_results=50,expansions=['author_id','geo.place_id'])
    #dic key:pair
    result=[]
    users = {u['id']: u for u in tweet.includes['users']}
    for t in tweet.data:
        user_tweet = {}
        user_tweet['tweet_id'] = t.id
        user_tweet['user_name'] = users.get(t.author_id)['name']
        user_tweet['tweet'] = t.text
        result.append(user_tweet)
    return json.dumps(result)

@app.route('/post',methods=["POST","GET"])
def post_tweet():
    info = request.get_json()['tweet']
    client = tweepy.Client(
        consumer_key=config.api_key, consumer_secret=config.api_key_secret,
        access_token=config.access_token, access_token_secret=config.access_token_secret
    )
    response = client.create_tweet(
        text=info
    )
    return json.dumps(response)

@app.route('/delete',methods=["POST","GET"])
def delete_tweet():
    info = request.get_json()['twitter_id']
    client = tweepy.Client(
        consumer_key=config.api_key, consumer_secret=config.api_key_secret,
        access_token=config.access_token, access_token_secret=config.access_token_secret
    )
    response = client.delete_tweet(info)
    return json.dumps(response)

if __name__=='__main__':
    app.run(debug=True,port=2000)
