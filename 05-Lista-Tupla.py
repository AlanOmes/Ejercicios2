# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) en una lista y la muestre por pantalla.

'''

lista = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
print (lista)

'''

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
# Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde 
# <asignatura> es cada una de las asignaturas de la lista.

'''

lista = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

for i in lista:
    print (f'Yo estudio {i}' )

'''

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las
# muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las
# asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

'''

materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []

for i in range(len(materias)):
    p = int (input (f'¿Qué nota sacaste en {materias[i]}?: '))
    notas.append(p)

print ('\r')

for i in range (len(materias)):
    print (f'En {materias[i]} has sacado {notas[i]}')

'''

# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en
# una lista y los muestre por pantalla ordenados de menor a mayor.

'''

lista = []

cant = int (input ('Escriba la cantidad de números que va a ingresar: '))

for i in range (cant):
    p = int (input ('Ingrese los números ganadores de la lotería: '))
    lista.append(p)

print ('\r')

lista.sort()
print (lista)

print ('---------') 

# Otra forma de hacerlo

lista2 = []
preguntar = True

while preguntar:
    c = (input ('Ingrese los números ganadores de la lotería (escriba "f" para finalizar): '))
    if c == 'f':
        preguntar = False
    else:
        lista2.append(c)
lista2.sort()

print ('\r')

print (lista2)

'''

# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden
# inverso separados por comas.

'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista[::-1]:
    print (i, end= ', ')

# Otra forma de hacerlo

print ('\r')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()

for i in numeros:
    print (i, end= ', ')

'''

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
# Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la
# lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
# usuario tiene que repetir.

'''

materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
r = []

for i in range (len(materias)):
    n = int (input (f'¿Cuánto sacaste en {materias[i]}?: '))
    if n <= 5:
        r.append(materias[i])

print ('\r')

for i in range (len(r)):
    print (f'Tienes que repetir {r[i]}')

'''

# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

'''

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

for i in range (len(abc), 1, -1):
    if i % 3 == 0:
        del abc[i-1]

print (abc)

'''

# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

'''

p = input ('Escriba una palabra: ')
p = list(p)

if p == (p[::-1]):
    print ('La palabra es palíndroma.')
else:
    print ('No es palíndroma.')

'''

# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene 
# cada vocal.

'''

p = input ('Escriba una palabra: ')
vocales = ['a', 'e', 'i', 'o', 'u']

for i in vocales:
    v = 0
    for l in p:
        if l == i:
            v = v + 1
    print (f'La vocal {i} aparece {v} veces.')

'''

# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre 
# por pantalla el menor y el mayor de los precios.

'''

precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort()

print (f'El precio menor es {precios[0]} y el precio mayor es {precios[6]}')

'''

# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su
# producto escalar.

