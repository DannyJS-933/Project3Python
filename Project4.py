#Vender un producto e indicar a que precion se debe vender para obtener la ganancia de un 30%


def articulo_comprado(laptop, mouse, monitor, keyboard):
    ingresarProducto = int(input('Para conocer el precio del articulo sin impuesto y el precio del articulo con el impuesto para tener una ganancia del 30% digite: \n'
                                 '1 para laptop \n'
                                 '2 para mouse \n'
                                 '3 para monitor \n'
                                 '4 para keyboard \n'
                                 'Opcion: '))

    if ingresarProducto == 1:
        impuesto = laptop * 0.3
        grandTotal = laptop + impuesto
        print(f'Sin impuesto {laptop} USD - Impuesto {impuesto} USD - Grand Total {grandTotal} USD')

    elif ingresarProducto == 2:
        impuesto = mouse * 0.3
        grandTotal = mouse + impuesto
        print(f'Sin impuesto {mouse} - Impuesto {impuesto} USD - Grand Total {grandTotal} USD')

    elif ingresarProducto == 3:
        impuesto = monitor * 0.3
        grandTotal = monitor + impuesto
        print(f'Sin impuesto {monitor} - Impuesto {impuesto} USD - Grand total {grandTotal} USD')
    elif ingresarProducto == 4:
        impuesto = keyboard * 0.3
        grandTotal = keyboard + impuesto
        print(f'Sin impuesto {keyboard} - Impuesto {impuesto} USD - Grand Total {grandTotal} USD')
    else:
        print('Dato ingresado no valido')
        print('Closing....')


articulo_comprado(400, 15, 200, 20)

