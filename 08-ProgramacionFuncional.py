# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una
# tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de 
# las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de
# la cesta y devolver el precio final de la cesta.

'''

def aplicar_descuento(precio, porcentaje):
    cantidadADescontar = (porcentaje * precio) / 100
    precioFinal = precio - cantidadADescontar
    return precioFinal

def aplicar_iva(precio, iva):
    cantidadADescontar = (iva * precio) / 100
    precioFinal = precio + cantidadADescontar
    return precioFinal

def aplicar_iva_o_descuentos(precios_y_porcentajes, funcion):
    total = 0
    for precio, descuento in precios_y_porcentajes.items():
        total += funcion(precio, descuento)
    return total        

lista_de_precios = {
    1000 : 20,
    500 : 10,
    100 : 1,
}

print (f'El precio de la compra tras aplicar los descuentos es: {aplicar_iva_o_descuentos(lista_de_precios, aplicar_descuento)}')
print (f'El precio de la compra tras aplicar el IVA es: {aplicar_iva_o_descuentos(lista_de_precios, aplicar_iva)}')

'''

# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente,
# exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y
# mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la
# función a esos enteros.

import math

def calculadora_cientifica():
    num = int (input('Ingrese el valor que quiera calcular: '))
    func = input ('Escriba la función que quiera aplicar (sen/cos/tan/exp/log): ')
    resultado = ''
    for i in range(1, num+1):
        if func == 'sen':
            seno = math.sin(i)
            resultado += (f'sen {str(i)} = {str(seno)}\n') 
    return resultado
print (calculadora_cientifica()) 