#!/usr/bin/env python
# coding: utf-8



from pymongo import MongoClient
import pandas as pd

client = MongoClient("149.165.172.75", 60000)
db = client.shardDB

collection = db["asofashion_2"]
collection2 = db["asofashion_clean"]

data = pd.read_csv("/home/exouser/spark_pyjobs/data_generator/Asofashion.csv")
print(data.shape)
print(data.columns)
final_data = data[['product_id', 'brand_name', 'title', 'current_price',
       'previous_price', 'colour', 'currency', 'rrp', 'productCode',
       'productType', 'gender']].copy()

print(final_data.shape)
collection.insert_many(final_data.sample(1000).to_dict('records'))
