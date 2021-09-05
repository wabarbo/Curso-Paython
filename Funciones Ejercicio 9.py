#*****Funciones 9*****
print('\nFunciones Ejercicio # 09\n')

lista = [2, 3, 5,7]

def esprimo (numero):
    if numero <=1:
        return False
    elif numero ==2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


numero = int(input(('Ingrese un número entero menor de 50--> ')))



if numero >= 50 or type(numero) is not int:
    exit("Debe ser un número entero menor de 50")


resultado = esprimo(numero)

if resultado == True:
    print(f'El número {numero} es primo')
else:
    print(f'El número {numero} no es primo')





