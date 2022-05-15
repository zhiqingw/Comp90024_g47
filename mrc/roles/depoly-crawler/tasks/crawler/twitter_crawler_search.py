import argparse
import tweepy
import json
import couchdb
import variables
import sys
import requests





def crawler_search(couch):
    db = couch['search_and_stream_tweets']
    useless_db = couch['useless_search_tweets']
    # initiate clinet
    client = tweepy.Client(bearer_token=bearer_token)

    query = 'melbourne'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['geo'], max_results=100)

    for i in tweets.data:
        id = i.data['id']
        text = i.data['text']
        data = {"id": id, "text": text}
        if 'geo' in i.data.keys() and 'coordinates' in i.data['geo'].keys():
            res = requests.get(url=('http://admin:admin@172.26.134.66:5984/search_and_stream_tweets/' + str(id)))
            # remove duplicates
            if res.ok:
                pass
            else:
                geo = i.data['geo']
                data = {"_id": id, "id": id, "geo": geo, "text": text}
                comb = json.dumps(data)
                db_line = json.loads(comb)
                db.save(db_line)
        else:
            comb = json.dumps(data)
            db_line = json.loads(comb)
            useless_db.save(db_line)


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

    while (True):
        crawler_search(couch)
