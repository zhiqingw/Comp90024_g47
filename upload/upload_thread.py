

#https://www.geeksforgeeks.org/multithreading-python-set-1/


import couchdb
import json
# couch = couchdb.Server("http://172.26.134.66:5984") 

import threading
  
def save_to_db(lower, upper):
    """
    function to save to db from range lower to upper
    """

    print("into running")
    couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')

    print("loaded couch")
    # page 42 



    db = couch['twenty_gig_file_tweets']
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
        elif((counter>lower) & (counter<upper)): 
            #print(row)
            print(counter)
            data = row[:-2]
            db_line = json.loads(data)
            db.save(db_line)

  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=save_to_db, args=(0,100000))
    t2 = threading.Thread(target=save_to_db, args=(100001,200000))
    t3 = threading.Thread(target=save_to_db, args=(2000001,300000))
    t4 = threading.Thread(target=save_to_db, args=(300001,400000))
    t5 = threading.Thread(target=save_to_db, args=(400001,500000))
    t6 = threading.Thread(target=save_to_db, args=(500001,600000))
    t7 = threading.Thread(target=save_to_db, args=(600001,700000))
    t8 = threading.Thread(target=save_to_db, args=(700001,800000))
    t9 = threading.Thread(target=save_to_db, args=(8000001,900000))
    t10 = threading.Thread(target=save_to_db, args=(900001,1000000))
    t11 = threading.Thread(target=save_to_db, args=(1000001,1100000))
    t12 = threading.Thread(target=save_to_db, args=(1100001,1200000))
    t13 = threading.Thread(target=save_to_db, args=(1200001,1300000))
    t14 = threading.Thread(target=save_to_db, args=(1300001,1400000))
    t15 = threading.Thread(target=save_to_db, args=(14000001,1500000))
    t16 = threading.Thread(target=save_to_db, args=(1500001,1600000))
    t17 = threading.Thread(target=save_to_db, args=(1600001,1700000))
    t18 = threading.Thread(target=save_to_db, args=(1700001,1800000))
    t19 = threading.Thread(target=save_to_db, args=(1800001,1900000))
    t20 = threading.Thread(target=save_to_db, args=(1900001,2000000))
    t21 = threading.Thread(target=save_to_db, args=(20000001,2100000))
    t22 = threading.Thread(target=save_to_db, args=(2100001,2200000))
    t23 = threading.Thread(target=save_to_db, args=(2200001,2300000))
    t24 = threading.Thread(target=save_to_db, args=(2300001,2400000))
    t25 = threading.Thread(target=save_to_db, args=(2400001,2500000))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 1
    t3.start()
    # starting thread 2
    t4.start()
    # starting thread 1
    t5.start()
    # starting thread 2
    t6.start()
    # starting thread 1
    t7.start()
    # starting thread 2
    t8.start()
    # starting thread 1
    t9.start()
    # starting thread 2
    t10.start()
    # starting thread 1
    t11.start()
    # starting thread 2
    t12.start()
    # starting thread 1
    t13.start()
    # starting thread 2
    t14.start()
    # starting thread 1
    t15.start()
    # starting thread 2
    t16.start()
    # starting thread 1
    t17.start()
    # starting thread 2
    t18.start()
    # starting thread 1
    t19.start()
    # starting thread 2
    t20.start()
    # starting thread 1
    t21.start()
    # starting thread 2
    t22.start()
    # starting thread 1
    t23.start()
    # starting thread 2
    t24.start()
    # starting thread 2
    t25.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # wait until thread 3 is completely executed
    t3.join()
    # wait until thread 4 is completely executed
    t4.join()
    # wait until thread 5 is completely executed
    t5.join()
    # wait until thread 6 is completely executed
    t6.join()
    # wait until thread 1 is completely executed
    t7.join()
    # wait until thread 2 is completely executed
    t8.join()
    # wait until thread 3 is completely executed
    t9.join()
    # wait until thread 4 is completely executed
    t10.join()
    # wait until thread 5 is completely executed
    t11.join()
    # wait until thread 6 is completely executed
    t12.join()
    # wait until thread 1 is completely executed
    t13.join()
    # wait until thread 2 is completely executed
    t14.join()
    # wait until thread 3 is completely executed
    t15.join()
    # wait until thread 4 is completely executed
    t16.join()
    # wait until thread 5 is completely executed
    t17.join()
    # wait until thread 6 is completely executed
    t18.join()
    # wait until thread 1 is completely executed
    t19.join()
    # wait until thread 2 is completely executed
    t20.join()
    # wait until thread 3 is completely executed
    t21.join()
    # wait until thread 4 is completely executed
    t22.join()
    # wait until thread 5 is completely executed
    t23.join()
    # wait until thread 6 is completely executed
    t24.join()
    # wait until thread 6 is completely executed
    t25.join()

    # both threads completely executed
    print("Done!")


