import argparse
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
    if match_ip is None:
        return False
    else:
        for value in match_ip.groups():
            if int(value) > 255:
                return False
                break
    return result


# test valid port
def valid_port(port_num):
    if (len(port_num) <= 5) & (port_num.isnumeric()):
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
        if 'geo' in i.data.keys() and 'coordinates' in i.data['geo'].keys():
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

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help="i stands for ip address")
    parser.add_argument('-p', help="p stands for port")
    args = parser.parse_args()
    if args.i and args.p:
        ip_address = str(args.i)
        port = str(args.p)
    else:
        print("missing input, need -p -i")
        sys.exit()

    if not (valid_IP_Address(ip_address) and valid_port(port)):
        print("invalid input, check your ip address and port")
        sys.exit()

    # bearer_token
    bearer_token = variables.bearer_token1

    # initiate database access
    access_ip = "http://" + variables.username + ":" + variables.password + "@" + ip_address + ":" + port + "/"
    couch = couchdb.Server(access_ip)

    while (True):
        crawler_search(couch)
