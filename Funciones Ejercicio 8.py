#*****Funciones 8*****
print('\nFunciones Ejercicio # 08\n')


def sumarvalores(a,b,c):

    return a+b+c

def participacion(a,b,c,aporteglobal):
    parta= a / aporteglobal * 100
    partb= b/aporteglobal * 100
    partc= c/aporteglobal * 100
    return parta, partb, partc


a = float(input(('Ingrese el aporte para A-->¢ ')))
b = float(input(('Ingrese el aporte para B-->¢ ')))
c = float(input(('Ingrese el aporte para C-->¢ ')))


aporteglobal= sumarvalores(a,b,c)
parta, partb, parc=participacion(a,b,c,aporteglobal)

print(f'El aporte global es de ¢{aporteglobal}: (A) aporta ¢{a} que corresponde al {round(parta,2)}%, (B) aporta ¢{b} que corresponde al {round(partb,2)}% y (C) aporta ¢{c} que corresponde al {round(parc,2)}%')



