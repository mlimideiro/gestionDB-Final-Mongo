from conection import *
from create import *




usuario.insert_one(
    {
        'estado' : True,
        'cuit_cuil' : '2020222022',
        'dni' : '20222022',
        'nombre' : 'George',
        'apellido' : 'Bruno',
        'razon_social' : '',
        'telefono' : '2496032565',
        'email' : 'gbruno@nomail.com',
        'usuario_tipo' : 'individuo',
        'nombre_usuario' : 'gbruno',
        'password' : '123456'
    }
)

usuario.insert_one(
    {
        'estado' : True,
        'cuit_cuil' : '2326659544',
        'dni' : '26659544',
        'nombre' : 'Lucas',
        'apellido' : 'Salvatori',
        'razon_social' : '',
        'telefono' : '2496598556',
        'email' : 'lucas_salva@gmail.com',
        'usuario_tipo' : 'individuo',
        'nombre_usuario' : 'lucas_salva',
        'password' : '111111'
    }
)

cuentas_info.insert_one(
    {
        'cbu' : '69696969',
        'saldo' : 5500,
        'sucursal' : 'tandil',
        'tipo_cuenta' : 'caja_ahorro',
        'fecha_apertura' : '2022-05-20',
        'estado' : True,
        'nombre_usuario' : 'gbruno'
    }
)

cuentas_info.insert_many( [
    {
        'cbu' : '45645644',
        'saldo' : 7000,
        'sucursal' : 'tandil',
        'tipo_cuenta' : 'caja_ahorro_dolares',
        'fecha_apertura' : '2022-04-10',
        'estado' : True,
        'nombre_usuario' : 'gbruno'
    },
    {
        'cbu' : '98989898',
        'saldo' : 17000,
        'sucursal' : 'tandil',
        'tipo_cuenta' : 'caja_ahorro_dolares',
        'fecha_apertura' : '2021-09-19',
        'estado' : True,
        'nombre_usuario' : 'lucas_salva'
    }
] )


cuentas_movimientos.insert_many( [
    {
        'monto' : 2600,
        'fecha_movimiento' : '2022-06-14',
        'moneda_tipo' : 'pesos',
        'comision' : 120,
        'tipo_cuenta' : 'caja_ahorro',
        'estado' : True,
        'nombre_usuario' : 'gbruno'
    },
        {
        'monto' : 1400,
        'fecha_movimiento' : '2022-06-09',
        'moneda_tipo' : 'pesos',
        'comision' : 100,
        'tipo_cuenta' : 'caja_ahorro',
        'estado' : True,
        'nombre_usuario' : 'gbruno'
    },
            {
        'monto' : 9800,
        'fecha_movimiento' : '2022-07-29',
        'moneda_tipo' : 'dolares',
        'comision' : 200,
        'tipo_cuenta' : 'caja_ahorro_dolares',
        'estado' : True,
        'nombre_usuario' : 'gbruno'
    }
] )
