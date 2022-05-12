from ipaddress import ip_address
import tweepy
import json 
import couchdb
import variables
import sys
import re 

# test valid ip address
# https://thispointer.com/check-if-a-string-is-a-valid-ip-address-in-python/ 
def valid_IP_Address(ip_address_string):
    result = True
    match_ip = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip_address_string)
    if  match_ip is None:
        return False
    else:
        for value in match_ip.groups():
            if int(value) > 255:
                return False
                break
    return result

# test valid port
def valid_port(port_num):
    if ((len(port_num)== 4) & (port_num.isnumeric())): 
        return True
    return False




def crawler_search(couch):
    db = couch['search_tweets']
    useless_db = couch['useless_search_tweets']
    # initiate clinet
    client = tweepy.Client(bearer_token=bearer_token)

    query = 'melbourne'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['geo'], max_results=100)

    for i in tweets.data:
        id = i.data['id']
        text = i.data['text']
        data = {"id": id, "text": text}
        if 'geo' in i.data.keys():
            geo = i.data['geo']
            data = {"id": id, "geo": geo, "text": text}
            comb = json.dumps(data)
            db_line = json.loads(comb)
            db.save(db_line)
        else:
            comb = json.dumps(data)
            db_line = json.loads(comb)
            useless_db.save(db_line)



if __name__ == "__main__":

    #read command line 
    args = sys.argv[1:]

    if (len(args) != 4):
        print("wrong input length: please use format -i <ip_adress> -p <port>")
        sys. exit()
    elif (args[0] != "-i"): 
        print("wrong format: please use format -i <ip_adress> -p <port>")
        sys. exit()
    elif (args[2] != "-p"): 
        print("wrong format: please use format -i <ip_adress> -p <port>")
        sys. exit()
    elif (not valid_IP_Address(args[1])):
        print("invalid IP Adress: please use format XXX.XXX.XXX.XXX, input format -i <ip_adress> -p <port>")
        sys. exit()
    elif (not valid_port(args[3])):
        print("invalid port: port needs to be 4 digits, for example 5000, input format -i <ip_adress> -p <port>")
        sys. exit()
    else: 
        ip_address = args[1]
        port = args[3]

    # bearer_token
    bearer_token = variables.bearer_token
    # consumer key and consumer secret key
    consumer_key = variables.consumer_key
    consumer_secret = variables.consumer_secret
    # access token and access secret token
    access_token = variables.access_token
    access_token_secret = variables.access_token_secret

    # initiate database access
    access_ip = "http://" + variables.username + ":" + variables.password +"@" + ip_address + ":" + port + "/"
    couch = couchdb.Server(access_ip)

    while(True):
        crawler_search(couch)

