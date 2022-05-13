import tweepy
import json 
import couchdb


def crawler_search(couch):
    db = couch['search_tweets']
    useless_db = couch['useless_search_tweets']
    # initiate clinet
    client = tweepy.Client(bearer_token=bearer_token)

    query = 'melbourne'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['geo'], max_results=100)

    for i in tweets.data:
        id = i.data['id']
        text = i.data['text']
        data = {"id": id, "text": text}
        if 'geo' in i.data.keys():
            geo = i.data['geo']
            data = {"id": id, "geo": geo, "text": text}
            comb = json.dumps(data)
            db_line = json.loads(comb)
            db.save(db_line)
        else:
            comb = json.dumps(data)
            db_line = json.loads(comb)
            useless_db.save(db_line)



if __name__ == "__main__":

    # bearer_token
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAMzWcAEAAAAAgv5MpTF1XRA0DAmoZxXPMxZqetg%3DyIh6UFDUfB5OHgzrofiJC6II254QDdO7Qdp9XEDtOXFMpkiROv"

    # consumer key and consumer secret key
    consumer_key = "khJZGL8dgSNqbLMWqwF1ThApo"
    consumer_secret = "m83j60DwamMdzESa1qt3M4vaPzsGw1F9kwZFLagTT9XB2RKKNO"

    # access token and access secret token
    access_token = "1521136048264425473-v0qMhh8K40exTZu0fl4JJOM6wCEW0z"
    access_token_secret = "LQ3BrS0Zz7NmbpJW6WWs3lFBdyY3yXeQPygTxCJQXdf7B"

    # initiate database access
    couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')

    while(True):
        crawler_search(couch)

