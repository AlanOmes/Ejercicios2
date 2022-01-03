# Escribir una funcion que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una
# tercera funcion que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de 
# las funciones anteriores, y utilice la funcion pasada para aplicar los descuentos o el IVA a los productos de
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

# Escribir una funcion que simule una calculadora cientifica que permita calcular el seno, coseno, tangente,
# exponencial y logaritmo neperiano. La funcion preguntara al usuario el valor y la funcion a aplicar, y
# mostrara por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la
# funcion a esos enteros.

'''

import math
import numpy as np

def calculadora_cientifica():
    num = int (input('Ingrese el valor que quiera calcular: '))
    func = input ('Escriba la funcion que quiera aplicar (sen/cos/tan/exp/log): ')
    func = func.lower()
    resultado = ''
    for i in range(1, num+1):
        if func == 'sen':
            seno = math.sin(i)
            resultado += (f'sen {str(i)} = {str(seno)}\n')
        elif func == 'cos':
            coseno = math.cos(i)
            resultado += (f'cos {str(i)} = {str(coseno)}\n')
        elif func == 'tan':
            tangente = math.tan(i)
            resultado += (f'tan {str(i)} = {str(tangente)}\n')
        elif func == 'exp':
            exponencial = np.exp(i)
            resultado += (f'exp {str(i)} = {str(exponencial)}\n')
        elif func == 'log':
            logaritmo = math.log(i)
            resultado += (f'log {str(i)} = {str(logaritmo)}\n')
    return resultado

print (calculadora_cientifica())

'''

# Escribir una funcion que reciba otra funcion y una lista, y devuelva otra lista con el resultado de aplicar
# la funcion dada a cada uno de los elementos de la lista.

'''

import math
import numpy as np

def calculadora_cientifica(pregunta, num):
    if pregunta == 'sen':
        resultado = math.sin(num)    
    elif pregunta == 'cos':
        resultado = math.cos(num)
    elif pregunta == 'tan':
        resultado = math.tan(num)
    elif pregunta == 'exp':
        resultado = np.exp(num)
    elif pregunta == 'log':
        resultado = math.log(num)
    return resultado

def aplicar_funcion_en_lista(preg, funcion, lista):
    resultados = []
    for i in lista:
        r = funcion(preg, i)
        resultados.append(r)
    return resultados

l = [1, 2, 3, 4, 5]
func = input ('Escriba la funcion que quiera aplicar (sen/cos/tan/exp/log): ')
func = func.lower()

print (aplicar_funcion_en_lista(func, calculadora_cientifica, l)) 

'''

# Escribir una funcion que reciba otra funcion booleana y una lista, y devuelva otra lista con los elementos de
# la lista que devuelvan True al aplicarles la funcion booleana.

'''

def numero_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def devolver_numeros_pares(funcion, numeros):
    pares = []
    for i in numeros:
        if funcion(i) == True:
            pares.append(i)
    return pares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (devolver_numeros_pares(numero_par, lista))

'''

# Escribir una funcion que reciba una frase y devuelva un diccionario con las palabras que contiene y su 
# longitud.

'''

def palabras_y_longitud(frase):
    palabras = {}
    frase = frase.split()
    for i in frase:
        palabras[i] = len(i)
    return palabras

f = 'hola como estas'

print (palabras_y_longitud(f)) 

'''

# Escribir una funcion reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas 
# notas.

# YO LO HICE CON DICCIONARIO EN LUGAR DE LISTA

'''

def calificaciones(notas):
    for i in notas:
        if notas[i] >= 6:
            notas[i] = 'Aprobado'
        else:
            notas[i] = 'Desaprobado'
    return notas

n = {
    'Matematicas' : 6,
    'Lengua' : 5,
    'Historia' : 1,
    'Geografia' : 7,
    'Quimica' : 9,
}

print (calificaciones(n))

'''

# Escribir una funcion reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro 
# diccionario con las asignaturas en mayusculas y las calificaciones correspondientes a las notas.

'''

def calificaciones(notas):
    calificaciones = {}
    for i in notas:
        if notas[i] >= 6:
            calificaciones[i.upper()] = 'Aprobado'
        else:
            calificaciones[i.upper()] = 'Desaprobado'
    return calificaciones

n = {
    'Matematicas' : 6,
    'Lengua' : 5,
    'Historia' : 1,
    'Geografia' : 7,
    'Quimica' : 9,
}

print (calificaciones(n))

'''

# Escribir una funcion reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro 
# diccionario con las asignaturas en mayusculas y las calificaciones correspondientes a las notas aprobadas.

'''

def calificaciones(notas):
    aprobadas = {}
    for i in notas:
        if notas[i] >= 6:
            aprobadas[i.upper()] = notas[i]
    return aprobadas

n = {
    'Matematicas' : 6,
    'Lengua' : 5,
    'Historia' : 1,
    'Geografia' : 7,
    'Quimica' : 9,
}

print (calificaciones(n))

'''

# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

# [{'anio': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
# {'anio': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
# {'anio': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
# {'anio': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
# {'anio': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

# Construir una funcion que permita hacer busqueda de inmuebles en funcion de un presupuesto dado. La funcion
# recibira como entrada la lista de inmuebles y un precio, y devolvera otra lista con los inmuebles cuyo precio
# sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
# diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente formula
# en funcion de la zona:

# -  Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
# -  Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5

inmuebles = [
{'anio': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'anio': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'anio': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'anio': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'anio': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def agregar_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones' * 5000 + int(piso['garaje']) * 15000]) * (1 - (2020 - piso['anio']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso


    