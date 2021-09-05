#*****Funciones 4*****
print('\nFunciones Ejercicio # 04\n')

def preciofinal (precio):

    precio = precio * (1+0.30)
    return precio



costo = float(input(('Ingrese el costo del artículo-->¢')))

resultado = preciofinal(costo)

print(f'\nLa tienda compra el artículo a ¢{costo} y lo vende a ¢{resultado}')

