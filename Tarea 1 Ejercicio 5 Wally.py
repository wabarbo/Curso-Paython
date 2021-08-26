#Tarea 1 Ejercicio 5 Wally Barrios Bonilla

#Inicialización de variables
viejas = 4

#Inicialización de constantes
descuento = 0.5
precio = 99.99

#Cálculo del precio con descuento
preciocondescuento = precio * descuento

#Salida en consola para el usuario
print(f'El precio habitual de una galleta es ¢{precio}. El descuento que se hace por no ser fresca es del {descuento*100}%.')
print(f'El costo final por las {viejas} galletas que no fueron frescas es de ¢{viejas*preciocondescuento}.')