#Digitar un nuemero menor a 50 y confirmar si es primo o no

def idetificar_si_es_primo():
    numero = int(input('Digite un numero menor a 50: '))

    if numero < 50:
        for i in range(1, numero // 2):
            if (numero % i) == 0:
                print(f'{numero} no es un numero primo')
                break
            else:
                print(f'{numero} es un numero primo')
                break
    else:
        print('Numero mayor a 50')


idetificar_si_es_primo()

