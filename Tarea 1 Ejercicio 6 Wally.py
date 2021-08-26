#Tarea 1 Ejercicio 6 Wally Barrios Bonilla
# Escribir el código que lea el número de teclados y mouse vendidos en el último período
# y calcule el peso total del paquete que será enviado

#Inicialización de constantes. El peso es dado en gramos
pesomouse = 75
pesoteclado = 200

#Inicialización de variables. Cantidades vendidas en el último período ingresadas por el usuario

mouse= 4
teclado= 5

#Cálculo peso del paquete
pesototal=(mouse*pesomouse)+(teclado*pesoteclado)

#Salida por pantalla al usuario
print(f'El peso total de las cantidades vendidas es de {pesototal} gramos.')
