from ipaddress import ip_address
import tweepy
import json 
import couchdb
import variables

class IDPrinter(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        db = couch['stream_tweets']
        useless_db = couch['useless_stream_tweets']

        id = tweet.data['id']
        text = tweet.data['text']
        data = {"id": id, "text": text}
        if 'geo' in tweet.data.keys():
            geo = tweet.data['geo']
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

    streaming_client = tweepy.StreamingClient(bearer_token)
    printer = IDPrinter(bearer_token)
    printer.sample()

