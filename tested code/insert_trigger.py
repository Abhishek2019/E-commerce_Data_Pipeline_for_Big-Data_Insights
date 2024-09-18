from pymongo import MongoClient
from LockQueue_module import LockQueue
import pandas as pd
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient("149.165.172.75", 60000)
db = client.shardDB

collection = db["asofashion_2"]

# try:
with collection.watch([{"$match": {"operationType": "insert"}}]) as stream:
    for insert_doc in stream:
        lq = LockQueue()
        while True:
            
            check = lq.write_queue([insert_doc["fullDocument"]])
            if check:
                break
        
            
# except Exception as err:
#     # The ChangeStream encountered an unrecoverable error or the
#     # resume attempt failed to recreate the cursor.
#     print("Error : occured ", err)