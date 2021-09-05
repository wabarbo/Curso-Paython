#*****Funciones 3*****
print('\nFunciones Ejercicio # 03\n')

def calculomasa (presion, volumen, temperatura):
    masa = (presion * volumen) / (0.37 * (temperatura + 460))
    return masa



presion = int(input(('Ingresa la presión-->')))

volumen = int(input(('Ingresa el volumen-->')))

temperatura = int(input(('Ingresa la temperatura-->')))

resultado = calculomasa(presion, volumen, temperatura)

print(f'\nPara una presión de {presion}, un volumen de {volumen} y una temperatura de {temperatura} el cálculo de la masa es de {resultado}')

