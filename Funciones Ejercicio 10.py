#*****Funciones 10*****
print('\nFunciones Ejercicio # 10\n')


import datetime


def obtenersegundos(s):
    L = s.split(':')
    if len(L) == 1:
             return L[0]

    elif len(L) == 2:
                 datee = datetime.datetime.strptime(s, "%M:%S")
                 return datee.minute * 60 + datee.second
    elif len(L) == 3:
             datee = datetime.datetime.strptime(s, "%H:%M:%S")
             return datee.hour * 3600 + datee.minute * 60 + datee.second

def diftiempo(resultado1, resultado2):
    return resultado1 - resultado2

tiempo1=input(('Ingrese el primer registro de tiempo en el formato HH:MM:SS--> '))
tiempo2=input(('Ingrese el segundo registro de tiempo en el formato HH:MM:SS--> '))

resultado1 = int(obtenersegundos(tiempo1))
resultado2 = int(obtenersegundos(tiempo2))

print(f'La diferencia en segundos entre los dos tiempos ingresados es: {diftiempo(resultado1,resultado2)}')


