import requests
import os
import pymongo


apikey = os.environ.get("N8NAPI")

headers = {"Content-Type": "application/json",
           "Authorization": f"token {apikey}"}

api_base_url = "http://localhost:5678/webhook-test/"
api_endpoint = "ac29895a-1c1f-46f6-8120-c78bbe04cf55"
api_url = f"http://localhost:5678/webhook-test/{api_endpoint}"

mon_db_user = os.environ.get("MONGODB_USER")
mon_db_pass = os.environ.get("MONGODB_PASS")
mon_client = pymongo.MongoClient(f"mongodb://{mon_db_user}:{mon_db_pass}@localhost:27017/")
mon_db = mon_client["n8n"]
mon_collection = mon_db["pillarposts"]
query = {
    "core_topics": {"$exists": True},
    "article_content": {"$exists": False}
}
docs = mon_collection.find(query).to_list()
for doc in docs:
    data = {
        'input_hash': doc['input_hash'],
        'data': doc['data'],
        'core_topics': doc['core_topics'],
        'thoughts': doc['thoughts']
    }

    res = requests.post(
        api_url,
        json=data, headers=headers)
    print(res)
