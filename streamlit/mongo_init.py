import pandas as pd
from pymongo import MongoClient

client=MongoClient("mongo")
names=client.list_database_names()
if "fifa23" in names:
    client.drop_database("fifa23")
db = client.fifa23
collection = db.joueur
df=pd.read_json('FIFA23.json')
DOCUMENTS = df.to_dict(orient='records')
collection.insert_many(DOCUMENTS)