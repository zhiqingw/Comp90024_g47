import argparse

import json
import couchdb
from tweepy import StreamingClient, StreamRule, Tweet

import variables
import sys
import requests




class TweetListener(StreamingClient):

    def on_tweet(self, tweet):
        db = couch['search_and_stream_tweets']
        useless_db = couch['useless_stream_tweets']

        id = tweet.data['id']
        text = tweet.data['text']
        data = {"id": id, "text": text}
        if 'geo' in tweet.data.keys() and 'coordinates' in tweet.data['geo'].keys():
            res = requests.get(url=('http://admin:admin@172.26.134.66:5984/search_and_stream_tweets/' + str(id)))
            # remove duplicates
            if res.ok:
                pass
            else:
                geo = tweet.data['geo']
                data = {"_id": id, "id": id, "geo": geo, "text": text}
                comb = json.dumps(data)
                db_line = json.loads(comb)
                db.save(db_line)
        else:
            comb = json.dumps(data)
            db_line = json.loads(comb)
            useless_db.save(db_line)

    def on_request_error(self, status_code):
        print(status_code)

    def on_connection_error(self):
        self.disconnect()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help="i stands for ip address")
    parser.add_argument('-p', help="p stands for port")
    args = parser.parse_args()
    if args.i and args.p:
        ip_address = str(args.i)
        port = str(args.p)
    else:
        print("missing input, need -p -i")
        sys.exit()



    # bearer_token
    bearer_token = variables.bearer_token1

    # initiate database access
    access_ip = "http://" + variables.username + ":" + variables.password + "@" + ip_address + ":" + port + "/"
    couch = couchdb.Server(access_ip)

    rules = [
        StreamRule(value="melbourne")
    ]

    # https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules
    # Remove existing rules
    client = TweetListener(bearer_token)
    resp = client.get_rules()
    if resp and resp.data:
        rule_ids = []
        for rule in resp.data:
            rule_ids.append(rule.id)

        client.delete_rules(rule_ids)

    # Validate the rule
    resp = client.add_rules(rules, dry_run=True)
    if resp.errors:
        raise RuntimeError(resp.errors)

    # Add the rule
    resp = client.add_rules(rules)
    if resp.errors:
        raise RuntimeError(resp.errors)

    # https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules
    print(client.get_rules())

    # https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream
    try:
        client.filter()
    except KeyboardInterrupt:
        client.disconnect()
