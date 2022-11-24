from pymongo import MongoClient

conection = MongoClient('localhost')

data_base = conection['mongo_banco']

