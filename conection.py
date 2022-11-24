from pymongo import MongoClient

conection = MongoClient('localhost',27017)


data_base = conection['mongo_banco']

