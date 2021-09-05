#*****Funciones 7*****
print('\nFunciones Ejercicio # 07\n')


def calcularpresupuesto(presupuesto):
    presu_ginecologia = presupuesto * 0.40
    presu_traumatologia = presupuesto * 0.30
    presu_padiatria = presupuesto * 0.30
    return presu_ginecologia, presu_traumatologia, presu_padiatria



presupuesto = float(input(('Ingrese el presupuesto anual de todas las áreas-->¢ ')))

x, y, z = calcularpresupuesto(presupuesto)

print(f'El presupuesto anual asignado es de ¢{presupuesto}. Para Ginecología el presupuesto es de ¢{x}. Para Traumatología el presupuesto es de ¢{y}. Para Padiatría el presupuesto es de ¢{z}')
