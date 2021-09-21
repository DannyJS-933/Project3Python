#Presion, volumen y temperatura, calcular la masa del aire
#formula: masa = (presion * volumen) / (0,37 *(temperatura + 460))

def calcular_masa():
    presion = int(input('Ingrese el valor de la presion: '))
    volumen = int(input('Ingrese el valor del volumen: '))
    temperatura = int(input('Ingrese el valor de la temperatura: '))
    formula = (presion * volumen) / (0.37 * (temperatura + 460))
    print(f'Al tratar de calcular la masa del aire, utilizamos la formula ({presion} * {volumen}) / (0.37 * ({temperatura} + 460)) y el resulato es {formula}')

calcular_masa()