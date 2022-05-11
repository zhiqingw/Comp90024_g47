from ipaddress import ip_address
import tweepy
import json 
import couchdb
import variables.py


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
    bearer_token = variables.bearer_token
    # consumer key and consumer secret key
    consumer_key = variables.consumer_key
    consumer_secret = variables.consumer_secret
    # access token and access secret token
    access_token = variables.access_token
    access_token_secret = variables.access_token_secret

    # initiate database access
    access_ip = "http://" + variables.username + ":" + variables.password +"@" + variables.ip_address + "/"
    couch = couchdb.Server(access_ip)

    while(True):
        crawler_search(couch)

