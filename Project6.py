#Calcular el incremento del salario sobre un 25%

def calcular_aumento():
    salarioActual = int(input('Ingrese su salario actual: '))
    aumento = 0.25
    salarioAumento = salarioActual * aumento
    salarioFinal = salarioAumento +salarioActual
    print(f'El aumento de su salario es de {salarioAumento} y el salario final es {salarioFinal}')


calcular_aumento()