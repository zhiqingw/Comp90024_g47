# Author:      Zhiqing Wu
# Student id:  931919
# Description: performing map reduce and stored the sentiment map to database

import requests
import couchdb
couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')

db = couch['sentiment_map']

db_name = "process_melb_tweet"
uname_list = requests.get('http://admin:admin@172.26.134.66:5984/' + db_name + '/_design/count_tweets_sentiment/_view/lga?group=true')
all_lga_and_sentiment = uname_list.json()["rows"]

res = requests.get(url='http://admin:admin@172.26.134.66:5984/sentiment_map/_all_docs')
lga_sentiment_map = {}

inner_melbourne_list = ['Carlton', 'Carlton North', 'Docklands', 'East Melbourne', 
'Flemington', 'Jolimont', 'Kensington', 'Melbourne', 'North Melbourne', 'Port Melbourne',
'Parkville','Southbank','South Wharf','South Yarra', 'West Melbourne'
]

for i in inner_melbourne_list:
    lga_sentiment_map[i] = {}

# loop through the mapreduce result
for i in all_lga_and_sentiment:
    lga = i['key'][1]
    if((i['key'][0] != None) & (lga != None)):
        sentiment = "neutral"
        if(i['key'][0] > 0):
            sentiment = "positive"
        elif(i['key'][0] < 0):
            sentiment = "negative"
        value = i['value']
        if(lga in lga_sentiment_map):
            lga_sentiment_map[lga][sentiment] = value
        # lga_sentiment_map[lga][sentiment] = value

sentiment_map = {}

# get the id if map already exist
if(res.json()['total_rows'] != 0):
    sentiment_map_id = res.json()['rows'][0]['id']
    sentiment_map = db[sentiment_map_id]

# store sentiment map
sentiment_map["map"] = lga_sentiment_map   

db.save(sentiment_map)
# print(all_lga_and_sentiment)
