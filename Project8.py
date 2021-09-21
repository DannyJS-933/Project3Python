#3 estudiantes invierten en un negocio, imprimir el % aportado por cada estudiante.

def empresa_aporte():

    a = int(input('Ingrese cantidad: '))
    b = int(input('Ingrese cantidad: '))
    c = int(input('Ingrese cantidad: '))

    total = a + b + c
    print(f'Cantidad ingresada {total} USD')
    primerAporte = (a / total) % 100 * 100
    print(f'El portentaje aportado es: {primerAporte} %')

    segundoAporte = (b / total) % 100 * 100
    print(f'El portentaje aportado es: {segundoAporte} %')

    tercerAporte = (c / total) % 100 * 100
    print(f'El portentaje aportado es: {tercerAporte} %')

empresa_aporte()