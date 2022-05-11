
# save tweets into couchdb 
from itertools import count
import couchdb
import json


print("into running")
couch = couchdb.Server('http://admin:admin@172.26.134.66:5984/')

print("loaded couch")

#db = couch.create('male_mental_health_vic_dhhs')
db = couch['male_mental_health_vic_dhhs']
print("created database")
#counter = 0
print("before upload")

f=open("lga_profilesdata2011-1000496935256049704.json", 'r',encoding='utf-8')


for row in f:
    db_line = json.loads(row)
    db.save(db_line)
print("finished upload")


