#*****Funciones 6*****
print('\nFunciones Ejercicio # 06\n')

def salariofinal (salario):

    salario = salario * (1+0.25)
    return salario



salario = float(input(('Ingrese el salario actual del funcionario-->¢')))

resultado = salariofinal(salario)

print(f'\nEl salario del funcionario es ¢{salario} y luego del incremento queda en ¢{resultado}')