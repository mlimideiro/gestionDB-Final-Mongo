from pymongo import MongoClient
from conection import *
from colecciones import *






print(data_base.list_collection_names())

cliente_coleccion.insert_one(
    {
        'direccion' : 'avellaneda'
    }
)


