from conection import *
from create import *


cliente_find_one = usuario.find_one(
    {
        'nombre': 'George'
    }
)
print('cliente_find_one:\n',cliente_find_one,'\n')



usuario_tipo_find_one = usuario.find_one(
    {
        'usuario_tipo' : 'individuo'
    }
)
print('usuario_tipo_find_one:\n',usuario_tipo_find_one,'\n')

usuario_tipo_find = usuario.find(
    {
        'usuario_tipo' : 'individuo'
    }
)
for usuario in usuario_tipo_find:
    print('usuario_tipo_find:\n',usuario,'\n')