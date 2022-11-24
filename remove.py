from conection import *
from create import *

cuentas_movimientos.delete_one( { 'tipo_cuenta' : 'caja_ahorro_dolares' })


#cuentas_movimientos.delete_many( { 'tipo_cuenta' : 'caja_ahorro' })
