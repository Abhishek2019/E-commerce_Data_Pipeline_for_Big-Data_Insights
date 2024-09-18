from pymongo import MongoClient
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.context import SparkContext
import string
import schedule
import time
import os

def cleaning_func(x):

    # lower case
    # replace & with and
    # remove punctuation
    
    x["title"] = x["title"].lower().replace("&","and").translate(str.maketrans('', '', string.punctuation))
    if str(x["current_price"]).lower() == 'nan':
        x["current_price"] = 0

    if str(x["previous_price"]).lower() == 'nan':
        x["previous_price"] = 0

    return x

def execute_spark_job():
    # print("-------------------------------- Job")
    client = MongoClient("149.165.172.75", 60000)
    db = client.shardDB
    
    c1 = db["asofashion_2"]
    c2 = db["asofashion_clean"]
    
    
    k = c1.aggregate([
    {"$match":{"_id":{"$exists":1}}},
    {"$lookup":{"from": "asofashion_clean",
                "localField":"_id",
                'foreignField' : '_id',
                "as":"missedWallet"
    }},
    {"$match":{"missedWallet.0":{"$exists":0}}}
    ]);
    

    input_data = list(k)
    if(len(input_data) != 0 ):
    
        spark = SparkSession \
        .builder \
        .appName("mongodbtest1") \
        .master("spark://10.1.174.144:7077")\
        .getOrCreate()

        clean_doc = spark.sparkContext.parallelize(input_data).map(cleaning_func).collect()
        # print(len(clean_doc))
        c2.insert_many(clean_doc)
        spark.stop()
        
    else:
        pass
        # print("data is upto date")

schedule.every(37).seconds.do(execute_spark_job)

while 1:
    schedule.run_pending()
    time.sleep(1)
