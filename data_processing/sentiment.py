from textblob import TextBlob
import pandas as pd

def data_processing(df):
	data = pd.DataFrame()
	data['coordinates'] = df['doc'].apply(lambda x: x['doc']['coordinates'])
	data = data.dropna(axis=0, subset=['coordinates'])
	data['long_lat'] = data['coordinates'].apply(lambda x: np.array(x['coordinates'])) ## geo coordinates

	data['lang'] = df['doc'].apply(lambda x: x['doc']['lang'])
	data = data[~data['lang'].isin(['und', None])]  # drop undefined language
 
	data['tweet'] = df['doc'].apply(lambda x: x['doc']['text']) ## get tweet text
 
	data['tweet_textBlob'] = data['tweet'].apply(lambda x: TextBlob(x)) ## turn text to TextBlob object

	data['sentiment'] = data['tweet_textBlob'].apply(lambda x: x.sentiment.polarity)

	return data

# df = pd.read_json("twitter-melb.json") # read twitter file

# data = data_processing(df)
