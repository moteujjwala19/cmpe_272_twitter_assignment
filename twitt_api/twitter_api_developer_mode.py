import tweepy
import config
import json
from flask import Flask,request
import requests
app = Flask(__name__)


# Below method is used to retrieve the tweets
# author - Chinmayi
@app.route("/get",methods=["POST","GET"])
def retrieve_tweets():
    client = tweepy.Client(bearer_token=config.bearer_token)
    query = request.get_json()['query']
    tweet = client.search_recent_tweets(query = query,max_results=50,expansions=['author_id'])
    #dic key:pair
    result=[]
    users = {u['id']: u for u in tweet.includes['users']}
    for t in tweet.data:
        user_tweet = {}
        user_tweet['tweet_id'] = str(t.id)
        user_tweet['user_name'] = users.get(t.author_id)['name']
        user_tweet['tweet'] = t.text
        result.append(user_tweet)
    print("res: ",result)
    return json.dumps(result)

# Below method is used to post the tweets
# author - Ujwala
@app.route('/post',methods=["POST","GET"])
def post_tweet():
    print("coming here");
    info = request.get_json()['tweet']
    print(info);
    client = tweepy.Client(
        consumer_key=config.api_key, consumer_secret=config.api_key_secret,
        access_token=config.access_token, access_token_secret=config.access_token_secret
    )
    response = client.create_tweet(
        text=info
    )
    return json.dumps(response)

# Below method is used to delete the tweets
# author - Suma
@app.route('/delete',methods=["POST","GET"])
def delete_tweet():
    info = request.get_json()['twitter_id']
    client = tweepy.Client(
        consumer_key=config.api_key, consumer_secret=config.api_key_secret,
        access_token=config.access_token, access_token_secret=config.access_token_secret
    )
    response = client.delete_tweet(info)
    return json.dumps(response)


@app.route('/my_tweet',methods=["POST","GET"])
def my_tweet():
    client = tweepy.Client(bearer_token=config.bearer_token)
    tweets = client.get_users_tweets(id=config.user_id);
    result=[]
    for t in tweets.data:
        user_tweet = {}
        user_tweet['tweet_id'] = str(t.id)
        user_tweet['user_name'] = "@AabbccddAa5"
        user_tweet['tweet'] = t.text
        result.append(user_tweet)
    return json.dumps(result)

if __name__=='__main__':
    app.run(debug=True,port=2000)
