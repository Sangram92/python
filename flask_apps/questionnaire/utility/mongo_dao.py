#Mongo DAO(Data access object)

from pymongo import MongoClient
import os
from bson.objectid import ObjectId
from utility.logger import logger

"""
    Use DAO to interface backend code with MongoDB
    get_one - retrieve one document from collection
    get_all - retrieve all documents from collection matching the condition
    update - update document in collection
    insert - insert document into collection
"""

host = os.environ.get('MONGO_HOST') or 'localhost'
port = os.environ.get('MONGO_PORT') or '27017'
username = os.environ.get('MONGO_USERNAME') or 'admin'
password = os.environ.get('MONGO_PASSWORD') or 'admin'
database = os.environ.get('MONGO_DB') or 'questionnaire'


print("hello.............", host, port, username, password, database)
client = MongoClient('mongodb://'+username+':'+password+'@'+host+':'+str(port)+'/'+database, maxPoolSize=200, waitQueueTimeoutMS=200)

# CRUD for Mongo

# Insert
def insert(collection, json):
    try:
        return str(client[database][collection].insert(json))
    except Exception as e:
        logger.error("Mongo Dao insert error: ", str(e))

# Update One
def update(collection, _id, dic):
    try:
        client[database][collection].update_one({'_id': ObjectId(_id)}, {"$set": dic}, upsert=True)
    except Exception as e:
        logger.error("Mongo Dao update error: ", str(e))

# Update Many
def update_many(collection, filters, update_value):
    try:
        client[database][collection].update(filters, {"$set": update_value})
    except Exception as e:
        logger.error("Mongo Dao update many error: ",str(e))

# Get all
def get_all(collection, filter_field, filter_value):
    try:
        #final_results = []
        results = client[database][collection].find({filter_field: filter_value})
        return [ res for res in results  ]
        # for result in results:
        #     final_results.append(str(result))
        return final_results
    except Exception as e:
        logger.error("Mongo Dao get all error: ",str(e))

# Get One
def get_one(collection, filter_field, filter_value):
    try:
        results = client[database][collection].find({filter_field: filter_value})
        for result in results:
            return result
    except Exception as e:
        logger.error("Mongo Dao get one error: ", str(e))

# Get collection
def get_collection(collection):
    try:
        results = client[database][collection].find({})
        return results
    except Exception as e:
        logger.error("Mongo Dao get collection error: ", str(e))

#search
def search_one(collection, json):
    try:
        results = client[database][collection].find(json)
        for result in results:
            return result
    except Exception as e:
        logger.error("Mongo Dao search one error: ", str(e))

# Get by id
def get_by_id(collection, _id):
    try:
        results = client[database][collection].find({"_id": ObjectId(_id)})
        for result in results:
            return result
    except Exception as e:
        logger.error("Mongo Dao get by id error: ", str(e))

# Delete
def delete(collection, _id):
    try:
        client[database][collection].delete_one({"_id": ObjectId(_id)})
    except Exception as e:
        logger.error("Mongo Dao delete error: ", str(e))

# Fetch ramdom records
def get_random_record(collection, query, size=1):
    try:
        record = client[database][collection].aggregate([
            { "$match": query },
            { "$sample": {"size": size} }
        ])
        print(record)
        return [r for r in record]
    except Exception as e:
        logger.error("Mongo Dao random error: ", str(e))
