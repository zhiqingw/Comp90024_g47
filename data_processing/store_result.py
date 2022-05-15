from email.base64mime import header_length
import json
import couchdb
import requests

from cal_tweets import get_sum_map
from cal_tweets import get_max_positve
from cal_tweets import get_max_negative
from aurin_hospital_bed import process_hospital
from aurin_pollutant import process_pollutant
from aurin_seat import process_seat

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
# print(max_positive_lga)
# print(max_negative_lga)

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
negative_lga['percentage'] = str(int(max_negative_lga['negative_percentage']*100)) + "%"
negative_lga['data'][0]['value'] = max_negative_lga['positive']
negative_lga['data'][1]['value'] = max_negative_lga['negative']
db.save(negative_lga)

# save hospital result
hospita = db['c414f40fbf9a3fa3d034c86b59c40922']
hospital_res = process_hospital('../data/hospital.csv')
lga_list = list(hospital_res.keys())
hospital_capacity = list(hospital_res.values())
positve_tweets_hospital = []
negative_tweets_hospital = []
for i in lga_list:
    neg = 0
    pos = 0
    if('negative' in sum_map[i].keys()):
        neg = sum_map[i]['negative']
    if('positive' in sum_map[i].keys()):
        pos = sum_map[i]['positive']
    positve_tweets_hospital.append(pos)
    negative_tweets_hospital.append(neg)
hospita['lga'] = lga_list
hospita['positive_tweets'] = positve_tweets_hospital
hospita['negative_tweets'] = negative_tweets_hospital
hospita['hospital_capacity'] = hospital_capacity
# print(hospita)
db.save(hospita)

# save pollutant result
pollutant = db['d428bceb0b93d1b0b4c7eb8dc0e1cfb9']
pollutant_res = process_pollutant('../data/pollutant.csv')
lga_list = list(pollutant_res.keys())
pollutant_emmision = list(pollutant_res.values())
positve_tweets_pollutant = []
negative_tweets_pollutant = []
for i in lga_list:
    neg = 0
    pos = 0
    if('negative' in sum_map[i].keys()):
        neg = sum_map[i]['negative']
    if('positive' in sum_map[i].keys()):
        pos = sum_map[i]['positive']
    positve_tweets_pollutant.append(pos)
    negative_tweets_pollutant.append(neg)
pollutant['lga'] = lga_list
pollutant['positive_tweets'] = positve_tweets_pollutant
pollutant['negative_tweets'] = negative_tweets_pollutant
pollutant['pollutant'] = pollutant_emmision
# print(pollutant)
db.save(pollutant)


# save restaurant result
seat = db['bcc28c0a43686e117e66fcac7c4cc8c7']
seat_res = process_seat('../data/seat.csv')
lga_list = list(seat_res.keys())
seat_capacity = list(seat_res.values())
positve_tweets_seat = []
negative_tweets_seat = []
for i in lga_list:
    neg = 0
    pos = 0
    if('negative' in sum_map[i].keys()):
        neg = sum_map[i]['negative']
    if('positive' in sum_map[i].keys()):
        pos = sum_map[i]['positive']
    positve_tweets_seat.append(pos)
    negative_tweets_seat.append(neg)
seat['lga'] = lga_list
seat['positive_tweets'] = positve_tweets_seat
seat['negative_tweets'] = negative_tweets_seat
seat['seat'] = seat_capacity
# print(seat)
db.save(seat)


# radar chart
radar = db['c414f40fbf9a3fa3d034c86b59c46938']
# positive scale
radar['data'][0]["name"] = max_positive_lga['lga']
positive_scale = []
positive_hospital = hospital_res[max_positive_lga['lga']]
positive_seat = seat_res[max_positive_lga['lga']]
positive_pollution = pollutant_res[max_positive_lga['lga']]
positive_scale.append(positive_hospital)
positive_scale.append(positive_seat)
positive_scale.append(positive_pollution)
radar['data'][0]["value"] = positive_scale
# negative scale
radar['data'][1]["name"] = max_negative_lga['lga']
negative_scale = []
negative_hospital = hospital_res[max_negative_lga['lga']]
negative_seat = seat_res[max_negative_lga['lga']]
negative_pollution = pollutant_res[max_negative_lga['lga']]
negative_scale.append(negative_hospital)
negative_scale.append(negative_seat)
negative_scale.append(negative_pollution)
radar['data'][1]["value"] = negative_scale
# indicator
radar['indicator'][0]['max']  = hospital_capacity[0]
radar['indicator'][1]['max'] =  seat_capacity[0]
radar['indicator'][2]['max']  = -pollutant_emmision[0]
# print(radar)
db.save(radar)




