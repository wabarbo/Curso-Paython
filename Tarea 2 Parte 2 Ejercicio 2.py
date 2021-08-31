#Actividad Asincrónica Wally Barrios Bonilla
import math

print('******************************\n*****Parte 2 Ejercicio 1******\n******************************')
print('Indicaciones: ¿Cuáles resultados se obtienen al evaluar las expresiones?')
#Item a
print(f'Item a, resultado: {2+3+1+2}')

#Item b
print(f'Item b, resultado: {2+3*1+2}')

#Item c
print(f'Item c, resultado: {(2+3)*1+2}')

#Item d
print(f'Item d, resultado: {(2+3)*(1+2)}')

#Item e
print(f'Item e, resultado: {+---6}')

#Item f
print(f'Item f, resultado: {-+-+6}')

#Item g
print(f'Item g, resultado: {1//2/4.0}')

#Item h
print(f'Item h, resultado: {1/2.0/4.0}')

#Item i
print(f'Item i, resultado: {1/2.0//4}')

#Item j
print(f'Item j, resultado: {1.0/2/4}')

#Item k
print(f'Item k, resultado: {4**.5}')

#Item l
print(f'Item l, resultado: {4.0**(1/2)}')

#Item m
print(f'Item m, resultado: {4.0**(1/2)+1/2}')

#Item n
print(f'Item n, resultado: {3e3/10}')

#Item o
print(f'Item o, resultado: {10/5e-3}')

#Item p
print(f'Item p, resultado: {4.0**(1.0/2)+1/2.0}')

#Item q
print(f'Item q, resultado: {10/5e-3+1}')

#Item r
print(f'Item d, resultado: {3/2+1}')

print('\n\n******************************\n*****Parte 2 Ejercicio 2******\n******************************')
print('Indicaciones: Traducir las expresiones a Python y utilizar el menor número posible de paréntesis')

#Item a: 2+(3*(6/2))
print(f'Item a, resultado: {2+3*6/2}')

#Item b: 4+6/2+3
print(f'Item b, resultado: {(4+6)/(2+3)}')

#Item c: (4/2)**5
print(f'Item c,resultado: {(4/2)**5}')

#Item d: (4/2)**5+1
print(f'Item d,resultado: {(4/2)**(5+1)}')

#Item e: (-3)**2
print(f'Item e, resultado: {(-3)**2}')

#Item f: -(3**2)
print(f'Item f, resultado: {-3 ** 2}')

print('\n\n******************************\n*****Parte 2 Ejercicio 3******\n******************************')
print('Indicaciones: Muestre el resultado de las siguientes operaciones')

#Item a:
print(f'Item a, resultado: {3467 + 56748 / 980}')

#Item b:
print(f'Item b, resultado: {673482 * -57843 * 87 / 8542}')

#Item c:
print(f'Item c, resultado: {265349 / 93864 * 3542 + 237895}')

#Item d:
print(f'Item d, resultado: {786757 * (65738 + 686958) / 45657 * (3576 + 95857)}')

print('\n\n******************************\n*****Parte 2 Ejercicio 4******\n******************************')
print('Indicaciones: Calcule con una única expresión el\nvalor absoluto del redondeo de -3.2. El resultado es 3.0\n ')

print(f'El valor absoluto de -3.2 es: {abs(math.ceil(-3.2))}')

print('\n\n******************************\n*****Parte 2 Ejercicio 5******\n******************************')
print('Indicaciones: Inicialice tres variables con diferentes valores.\n ')
var1 = 1
var2 = 2
var3 = 3

#Item a
var3= (var1 * var2)+ (var1/ var2)
print(f'Item a, resultado: El valor actual de Var3 es:{var3}')

#Item b
var1 *= 67 / 34
var2=87
print(f'Item b, resultado: El valor actual de Var1 es:{var1}. El valor actual de Var2 es:{var2}')

#Item c
var3 = (var1 * var2) + (var1 / var2)
print(f'Item c, resultado. El valor actual de var3 es:{var3}')

print('\n\n******************************\n*****Parte 2 Ejercicio 6******\n******************************')
print('Indicaciones: Evalúe el polinomio x4+x3+2x2-x en x=1.1.\n ')
x = 1.1
print(f'El resultado del polinomio es: {x ** 4 + x ** 3 + 2 * x ** 2 - x}')

print('\n\n******************************\n*****Parte 2 Ejercicio 7******\n******************************')
print('Indicaciones: Evalúe el polinomio x4+x3+(1/2)x2-x en x=10.\n ')
x = 10
print(f'El resultado del polinomio es: {x ** 4 + x ** 3 + (1/2) * x ** 2 - x}')

print('\n\n******************************\n*****Parte 2 Ejercicio 8******\n******************************')
print('¿Qué resultará de ejecutar las siguientes sentencias?')
x = 2
print(f'Item a, resultado de x=2 es:{x}')

x+=2
print(f'Item b, resultado de x+=2 es:{x}')

x += 2 - 2
print(f'Item c, resultado de x+=2-2 es:{x}')

x *=2
print(f'Item d, resultado de x*=2 es:{x}')

x *= 1 + 1
print(f'Item e, resultado de x*=1+1 es:{x}')

x /=2
print(f'Item f, resultado de x/=2 es:{x}')

x %=3
print(f'Item g, resultado de x%=3 es:{x}')

x /= 3 - 1
print(f'Item h, resultado de x/=3-1 es:{x}')

x -= 2 + 1
print(f'Item i, resultado de x-=2+1 es:{x}')

x -= 2
print(f'Item j, resultado de x-=2 es:{x}')

x**=3
print(f'Item k, resultado de x**=3 es:{x}')

print(f'Item l, resultado de x es:{x}')

print('\n\n******************************\n*****Parte 2 Ejercicio 9******\n******************************')
print('Instrucciones: Despliegue sobre consola las figuras mostradas a continuación')


valores=['* * * * * * *','*           *','*           *','*           *','*           *','*           *','* * * * * * *']
for k in valores:
    print(k)

triangulo=['      *      ','     * *     ','    *   *    ','   *     *   ','  *       *  ',' *         * ','* * * * * * *']
print('\n')
for t in triangulo:
    print(t)

rombo=['      *      ','     * *     ','    *   *    ','   *     *   ','  *       *  ',' *         * ',' *         * ','  *       *  ','   *     *   ','    *   *    ','     * *     ','      *      ']
print('\n')
for r in rombo:
    print(r)

flecha=['              *','               *','* * * * * * * * *','               *','              *']
print('\n')
for f in flecha:
    print(f)


##################################################

###########################
width, height = 11, 11
a, b = 5, 5
r = 5
EPSILON = 2.2

#[ '.' for x in range(width)]
map_ = [[ '.' for x in range(width)] for y in range(height)]

# draw the circle
for y in range(height):
    for x in range(width):
        # see if we're close to (x-a)**2 + (y-b)**2 == r**2
        if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
            map_[y][x] = '*'

# print the map
for line in map_:
    print(line)



#############
