# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

'''

palabra = input ('Escriba una palabra: ')

for i in range (10):
    print (palabra)

'''

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
# (desde 1 hasta su edad).

'''

edad = int (input ('Escriba su edad: '))

for i in range (1, edad+1):
    print (f'Has cumplido {i} años.')

'''

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números
# impares desde 1 hasta ese número separados por comas.

'''

num = int (input ('Escribir un número entero positivo: '))

for i in range (1, num+1, 2):
    print (i, end= ', ')

'''

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás
# desde ese número hasta cero separados por comas.

'''

num = int (input ('Escribir un número entero positivo: '))

for i in range (-num, 0):
    print (i * (-1), end= (', '))
    
'''

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

'''

c = float (input ('Escriba la cantidad a invertir: '))
i = int (input ('Escriba el porcentaje de interés anual: '))
a = int (input ('Escriba el número de años que va a realizar la inversión: '))

for j in range (1, a+1):
    interes = c * i / 100
    cap_ob = c + interes
    c = cap_ob 
    print (f'{j}º año: {cap_ob}') 

'''

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como 
# el de más abajo, de altura el número introducido.

'''

num = int (input ('Escriba un número entero: '))

for j in range (num + 1):
        for i in range (j):
         print ('*', end= (""))
        print ("")

'''

# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

'''

for i in range (1, 10 + 1):
    print (i, "* 1 =", i * 1)
    print (i, "* 2 =", i * 2)
    print (i, "* 3 =", i * 3)
    print (i, "* 4 =", i * 4)
    print (i, "* 5 =", i * 5)
    print (i, "* 6 =", i * 6)
    print (i, "* 7 =", i * 7)    
    print (i, "* 8 =", i * 8)
    print (i, "* 9 =", i * 9)
    print (i, "* 10 =", i * 10)
    print ("-------")

print ('-------------')

# Otra solución

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

'''

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como
# el de más abajo.

#      1
#      3 1
#      5 3 1
#      7 5 3 1
#      9 7 5 3 1

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por
# la contraseña hasta que introduzca la contraseña correcta.

'''

contraseña = 'b22eadc1'
preguntar = True

while preguntar:
    c = input ('Por favor, ingrese la contraseña: ')
    print ('\r')
    if c == contraseña:
        print ('Contraseña correcta.')
        preguntar = False
    else:
        print ('Contraseña incorrecta. Por favor, intente nuevamente.\r\n')

'''

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

'''

num = int (input ('Escriba un número entero mayor que 1: '))
primo = True

if num <= 1:
    print ('¡Le he pedido un número entero mayor que 1!')
else:
    for i in range (2, 11):
        if num % i == 0:
            if num != i:
                primo = False
    if primo == True:
        print (f'{num} es primo.')
    else:
        print (f'{num} no es primo.')

'''

# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la
# palabra introducida empezando por la última.

'''

pal = input ('Escriba una palabra: ')

for i in pal[::-1]:
    print (i)
    
'''

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el
# número de veces que aparece la letra en la frase.

'''

frase = input ('Escriba una frase: ')
letra = input ('Escriba una letra: ')
cant = frase.count(letra)

print (f'Cantidad de veces que aparece la letra "{letra}" en la frase: {cant}')

print ('---------')

# Otra forma de resolverlo

contador = 0

for i in frase:
    if i == letra:
        contador = contador + 1

print (f'Cantidad de veces que aparece la letra "{letra}" en la frase: {contador}')

'''

# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba
# “salir” que terminará.

'''

preguntar = True

while preguntar:
    f = input ('Escriba lo que quiera y se lo repetiré (para terminar el programa escriba "salir"): ')
    if f == 'Salir' or f == 'salir':
        print ('\r\nPrograma finalizado. Muchas gracias.')
        preguntar = False
    else:
        print ('\r')
        print (f)
        print ('\r')

'''