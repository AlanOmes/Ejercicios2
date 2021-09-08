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

materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
t = len(materias)


for i in range (t-1):
    nota = int (input (f'¿Qué nota sacaste en {materias[i]}: '))
    if nota >= 6:
        del materias[i]