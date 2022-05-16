# Author:      Zhiqing Wu
# Student id:  931919
# Description: sentiment map processing

import requests
# get the maximum positive lga
def get_max_positve(sum_map):
    max_positive_lga = {}
    lga_list = list(sum_map.keys())
    if len(lga_list) > 0:
        max_positive_lga['lga'] = lga_list[0]
        max_positive_lga['positive_percentage'] = sum_map[lga_list[0]]['positive_percentage']
        max_positive_lga['positive'] = sum_map[lga_list[0]]['positive']
        max_positive_lga['negative'] = sum_map[lga_list[0]]['negative']
        max_positive_lga['neutral'] = sum_map[lga_list[0]]['neutral']
    
    for i in lga_list:
        if sum_map[i]['positive_percentage'] > max_positive_lga['positive_percentage']:
            max_positive_lga['lga'] = i
            max_positive_lga['positive_percentage'] = sum_map[i]['positive_percentage']
            max_positive_lga['positive'] = sum_map[i]['positive']
            max_positive_lga['negative'] = sum_map[i]['negative']
            max_positive_lga['neutral'] = sum_map[i]['neutral']
    return max_positive_lga

# get the maximum negative lga
def get_max_negative(sum_map):
    max_negative_lga = {}
    lga_list = list(sum_map.keys())
    if len(lga_list) > 0:
        max_negative_lga['lga'] = lga_list[0]
        max_negative_lga['negative_percentage'] = sum_map[lga_list[0]]['negative_percentage']
        max_negative_lga['positive'] = sum_map[lga_list[0]]['positive']
        max_negative_lga['negative'] = sum_map[lga_list[0]]['negative']
        max_negative_lga['neutral'] = sum_map[lga_list[0]]['neutral']
    
    for i in lga_list:
        if sum_map[i]['negative_percentage'] > max_negative_lga['negative_percentage']:
            max_negative_lga['lga'] = i
            max_negative_lga['negative_percentage'] = sum_map[i]['negative_percentage']
            max_negative_lga['positive'] = sum_map[i]['positive']
            max_negative_lga['negative'] = sum_map[i]['negative']
            max_negative_lga['neutral'] = sum_map[i]['neutral']
    return max_negative_lga


# process the sentiment map
def get_sum_map(mel_tweets):
    sum_map = {}

    for i in mel_tweets.keys():
        sum_map[i] = {}
        neutral = 0
        positive = 0
        negative = 0
        if "positive" in mel_tweets[i]:
            positive += mel_tweets[i]['positive']
        if "negative" in mel_tweets[i]:
            negative += mel_tweets[i]['negative']
        if "neutral" in mel_tweets[i]:
            neutral += mel_tweets[i]['neutral']
        sum_map[i]['positive'] = positive
        sum_map[i]['negative'] = negative
        sum_map[i]['neutral'] = neutral
        if(positive + negative) != 0:
            sum_map[i]['positive_percentage'] = positive/(positive + negative + neutral)
            sum_map[i]['negative_percentage'] = negative/(positive + negative + neutral)
        else: 
            sum_map[i]['positive_percentage'] = 0
            sum_map[i]['negative_percentage'] = 0
    return sum_map

res = requests.get(url='http://admin:admin@172.26.134.66:5984/sentiment_map/_all_docs')
# print(res.json()['rows'][0]['id'])
id = res.json()['rows'][0]['id']
map = requests.get(url='http://admin:admin@172.26.134.66:5984/sentiment_map/' + id)
# print(map.json())

mel_tweets = map.json()['map']


sum_map = get_sum_map(mel_tweets)
get_max_positve(sum_map)
get_max_negative(sum_map)

# print(sum_map)