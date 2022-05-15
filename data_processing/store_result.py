import couchdb
import requests

from cal_tweets import get_sum_map
from cal_tweets import get_max_positve
from cal_tweets import get_max_negative

couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')
db = couch['result']
# get sentiment map
res = requests.get(url='http://admin:admin@172.26.134.66:5984/sentiment_map/_all_docs')
id = res.json()['rows'][0]['id']
map = requests.get(url='http://admin:admin@172.26.134.66:5984/sentiment_map/' + id)

mel_tweets = map.json()['mel_tweets']
stream_and_search = map.json()['stream_and_search']

sum_map = get_sum_map(mel_tweets, stream_and_search)
max_positive_lga = get_max_positve(sum_map)
max_negative_lga = get_max_negative(sum_map)
print(max_positive_lga)
print(max_negative_lga)

# save most positive lga
positve_lga = db['c414f40fbf9a3fa3d034c86b59c42a1f']
positve_lga['lga'] = max_positive_lga['lga']
positve_lga['percentage'] = str(max_positive_lga['positive_percentage']*100) + "%"
positve_lga['data'][0]['value'] = max_positive_lga['positive']
positve_lga['data'][1]['value'] = max_positive_lga['negative']
db.save(positve_lga)

# save most negative lga
negative_lga = db['c414f40fbf9a3fa3d034c86b59dd6583']
negative_lga['lga'] = max_negative_lga['lga']
negative_lga['percentage'] = str(max_negative_lga['negative_percentage']*100) + "%"
negative_lga['data'][0]['value'] = max_negative_lga['positive']
negative_lga['data'][1]['value'] = max_negative_lga['negative']
db.save(negative_lga)