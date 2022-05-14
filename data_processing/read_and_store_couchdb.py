from unittest.mock import sentinel
import couchdb
from sentiment import data_processing
from convert_geo import geo_convertor
import numpy as np
import pandas as pd
from textblob import TextBlob
couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')
db = couch['test']

for id in db:
    curr = db[id]
    # calculate the sentiment of this tweet
    text = curr['doc']['text']
    text_textBlob = TextBlob(text)
    sentiment = text_textBlob.sentiment.polarity
    curr["sentiment"] = sentiment

    # get the lga of the geo of this tweet
    coordinate = curr['doc']['coordinates']['coordinates']
    coordinate_format = str(coordinate[1]) +"," + str(coordinate[0])
    # print(coordinate_format)
    curr["lga"] = geo_convertor(coordinate_format)

    db.save(curr)
