import requests
import couchdb
# from textblob import TextBlob
couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')
# db = couch.create('sentiment-map')
db = couch['sentiment-map']
# 'http://admin:admin@172.26.134.66:5984/twenty_gig_tweets/_design/count_tweets_sentiment/_view/lga?group=true'
# http://admin:admin@172.26.134.66:5984/student/_design/info/_view/count?group=true
uname_list = requests.get('http://admin:admin@172.26.134.66:5984/twenty_gig_tweets/_design/count_tweets_sentiment/_view/lga?group=true')
all_lga_and_sentiment = uname_list.json()["rows"]

# print(res.json())
lga_sentiment_map = {}

for i in all_lga_and_sentiment:
    lga = i['key'][1]
    if((i['key'][0] != None) & (lga != None)):
        sentiment = "neutral"
        if(i['key'][0] > 0):
            sentiment = "positive"
        elif(i['key'][0] < 0):
            sentiment = "negative"
        value = i['value']
        if(lga not in lga_sentiment_map):
            lga_sentiment_map[lga] = {}
        lga_sentiment_map[lga][sentiment] = value

# print(lga_sentiment_map)

#get the id if map already exist
res = requests.get(url='http://admin:admin@172.26.134.66:5984/sentiment-map/_all_docs')
if(res.json()['total_rows'] != 0):
    sentiment_map_id = res.json()['rows'][0]['id']
    sentiment_map = db[sentiment_map_id]
    sentiment_map = lga_sentiment_map
else:
    db.save(lga_sentiment_map)






# res = requests.get(url='http://admin:admin@172.26.134.66:5984/test/_all_docs')
# print(res.json()['rows'][0]['id'])
