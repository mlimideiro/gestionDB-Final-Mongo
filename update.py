from conection import *
from create import *

usuario.update_one( {'telefono' : '2496032565'}, {'$set' : {'telefono' : '000000000'}  })

cliente_find = usuario.find_one(
    {
        'nombre': 'George'
    }
)
print('cliente_find:\n',cliente_find)


