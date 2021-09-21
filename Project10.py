#Ingresar horas, minutos, segundos y convertirlo a segundos

import  datetime

def time():
    hour = input('Ingrese una hora: ')
    minutes = input('Ingrese los minutos: ')
    segundos = input('Ingrese los segundos: ')
    milisegundos = input('Ingrese los milisegundos: ')
    fecha = '2021-09-20'
    tiempoIgresado = print(f'2021-09-20 {hour}:{minutes}:{segundos}:{milisegundos}')
    #print(tiempoIgresado)
    timeFormat = datetime.time.strftime(tiempoIgresado, '%H:%M:%S.%f')
    print(timeFormat.time())

time()
