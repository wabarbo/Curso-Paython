#*****Funciones 05*****
print('\nFunciones Ejercicio # 05\n')


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

def obtenertiempo(resultado1, resultado2, resultado3):

    totalsegundos = (resultado1 + resultado2 + resultado3) / 3

    hor = (int(totalsegundos / 3600))
    minu = int((totalsegundos - (hor * 3600)) / 60)
    seg = int(totalsegundos - ((hor * 3600) + (minu * 60)))

    print("En una semana cualquiera, el tiempo promedio es de: " + str(hor) + "h " + str(minu) + "m " + str(seg) + "s")





tiempo1=input(('Ingrese el tiempo para el lunes en el formato HH:MM:SS--> '))
tiempo2=input(('Ingrese el tiempo para el miércoles en el formato HH:MM:SS--> '))
tiempo3=input(('Ingrese el tiempo para el viernes en el formato HH:MM:SS--> '))

resultado1 = int(obtenersegundos(tiempo1))
resultado2 = int(obtenersegundos(tiempo2))
resultado3 = int(obtenersegundos(tiempo3))

print(f'Los tiempos ingresados son: lunes {tiempo1}, miércoles {tiempo2}, viernes {tiempo3}')

obtenertiempo(resultado1,resultado2, resultado3)






