from pymongo import MongoClient
from conection import *
from create import *

cliente_find = cliente_coleccion.find_one(
    {
        'nombre': 'Marcelo'
    }
)

print(cliente_find)