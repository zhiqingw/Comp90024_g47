import couchdb
from sentiment import data_processing
from convert_geo import geo_convertor
from textblob import TextBlob
import requests

couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')
db = couch['search_tweets']



res = requests.get(url='http://admin:admin@172.26.134.66:5984/search_tweets/_all_docs')
all_id = res.json()['rows']
# print(all_id)
for id in all_id:
    curr = db[id['id']]
    # skip the data already assign sentiment and lga
    # if(("sentiment" in curr) & ("lga" in curr)):
    #     print("exist: " + id['id'])
    #     continue
    
    text = ""
    coordinate_format = ""
    if("doc" in curr):
        text = curr['doc']['text']
        coordinate = curr['doc']['coordinates']['coordinates']
        coordinate_format = str(coordinate[1]) +"," + str(coordinate[0])
    else:
        text = curr['text']
        coordinate = curr['geo']['coordinates']['coordinates']
        coordinate_format = str(coordinate[1]) +"," + str(coordinate[0])


    # calculate the sentiment of this tweet
    text_textBlob = TextBlob(text)
    sentiment = text_textBlob.sentiment.polarity
    if(sentiment > 0):
        curr["sentiment"] = 1
    elif(sentiment < 0):
        curr["sentiment"] = -1
    else:
        curr["sentiment"] = 0


    # get the lga of the geo of this tweet
  
    try:
        curr["lga"] = geo_convertor(coordinate_format)
            
    except:        
        curr["lga"] = "unknown"
   

    print(curr)
    
    db.save(curr)
