import argparse
import json
import couchdb
import requests


if __name__ == "__main__":

    couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')
    from_db = couch['search_tweets']
    to_db = couch['search_and_stream_tweets']
    res = requests.get(url='http://admin:admin@172.26.134.66:5984/search_tweets/_all_docs')
    for id in res.json()['rows']:
        couch_id = id['id']
        tweetId = from_db[couch_id]['id']
        geo = from_db[couch_id]['geo']
        text = from_db[couch_id]['text']
        res = requests.get(url=('http://admin:admin@172.26.134.66:5984/search_and_stream_tweets/'+str(tweetId)))
        print(res)
        if res.ok:
            pass
        else:
            to_db.save({"_id": tweetId, "id": tweetId, "geo": geo, "text": text})
