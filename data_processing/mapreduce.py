import requests
# from textblob import TextBlob
# couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')
# db = couch['student']
# 'http://admin:admin@172.26.134.66:5984/twenty_gig_tweets/_design/count_tweets_sentiment/_view/lga?group=true'
# http://admin:admin@172.26.134.66:5984/student/_design/info/_view/count?group=true
uname_list = requests.get('http://admin:admin@172.26.134.66:5984/twenty_gig_tweets/_design/count_tweets_sentiment/_view/lga?group=true')
print(uname_list.json())





# res = requests.get(url='http://admin:admin@172.26.134.66:5984/test/_all_docs')
# print(res.json()['rows'][0]['id'])
