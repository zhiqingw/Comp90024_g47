

#https://www.geeksforgeeks.org/multithreading-python-set-1/


import couchdb
import json
# couch = couchdb.Server("http://172.26.134.66:5984") 

import threading
  
def save_to_db():
    """
    function to save to db from range lower to upper
    """

    print("into running")
    couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')

    print("loaded couch")
    # page 42 



    db = couch['twitter-melb']
    #db = couch.create('green')
    print("created database")
    #db.save('green_space_safety_visit_to_green_space_more_than_once_perwk-8898569845817672567.json')
    #print("loaded database")

    #counter = 0
    print("before upload")
    #with open("green_space_safety_visit_to_green_space_more_than_once_perwk-8898569845817672567.json") as jfile:



    #with open("twitter-melb.json") as jfile: 
    #    print("started upload")
    #    db_line = json.load(jfile)
    #    db.save(db_line)
        #for row in jfile:
            #print(row)
        #    db_line = json.load(row)
        #    db.save(db_line)
        #counter += 1
        #if (counter%10000 == 0):
        #    print(counter)

    f=open("twitter-melb.json", 'r',encoding='utf-8')


    counter = 0
    rows = 154405640

    for row in f: 
        counter += 1
        #print(counter)
        if (counter == 1): 
            print(row)
            #rows = (int) 14:
            #break 
        elif(counter == 2500002): 
            break
        else:
            #print(row)
            print(counter)
            data = row[:-2]
            db_line = json.loads(data)
            db.save(db_line)

  
if __name__ == "__main__":
    save_to_db()
    # both threads completely executed
    print("Done!")


