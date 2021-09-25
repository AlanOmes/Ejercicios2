# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

'''

def saludo():
    print ('¡Hola amiga!')

saludo() 

'''

# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

'''

def saludo(nombre):
    print (f'¡Hola {nombre}!')

nombre = 'Alan'
saludo(nombre) 

'''

# Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''

def factorial(num):
    f = 1
    for i in range (1, num+1):
        f *= i 
    return f

factorial(5)
factorial(4)
    
'''

# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
# cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función 
# sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

'''

def iva (num, p = 21):
    porcentaje = (p * num) / 100
    t = num + porcentaje
    return t

iva(100, 20)
iva (10)

'''

# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

'''

def media (l, c):
    m = 0
    for i in l:
        m += i
    return (m / c)

l = [1, 2, 3, 4, 5]

media(l, len(l))

'''

# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

'''

def cuadrado(l):
    l_c = []
    for i in l:
        c = i ** 2
        l_c.append(c)
    return l_c

l = [1, 2, 3, 4, 5]

print (cuadrado(l))

'''

# Juli

'''

def suma(a, b): 
    r = a + b # 2
    return r # 3

s =  suma(2, 2) # 1

if s % 2 == 0: # 4 
    print (f'{s} es par') # 5
else: # 4
    print (f'{s} es impar.') # 5

'''

# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su promedio,
# cuadrado y raíz cuadrada.

'''

def suma(l):
    s = 0
    for i in l:
        s += i
    return s

def calculos (l):
    cajeta = suma(l)
    total = {
        'promedio' : cajeta / len(l),
        'cuadrado' : cajeta ** 2,
        'raiz' : cajeta ** 0.5,
    }
    return total

l = [1, 2, 3, 4, 5]
print (calculos(l))

'''

# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en
# decimal.

'''

def binario_decimal(n):
    string = str(n)
    b = int(string, 2)
    return b

def decimal_binario(n):
    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2
    binario.reverse()
    return ''.join(binario)

print (binario_decimal(1101))
print (decimal_binario(13))

'''
# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida 
# o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".


'''

def validez(mail):
    mail = list(mail)
    valido = 0
    for i in mail:
        if i == '@':
            valido += 1
    if valido == 1:
        return True
    else:
        return False

mail = input ('Ingrese su mail: ')

if validez(mail) == True:
    print ('La dirección es válida.')
else:
    print ('La dirección es invalida.')

'''

# Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos 
# (utilizando una función que realice dicha suma).

'''

def suma_digitos(n):
    copia = n
    suma=0
    while copia != 0:
        digito = copia % 10
        suma = suma + digito
        copia = copia // 10
    return suma

n = int (input('Ingrese un número y sumaré sus dígitos: '))

while n != 0:
    t = suma_digitos(n)
    print (f'La suma de los dígitos de {n} es {t}')
    n = int (input('Ingrese un número y sumaré sus dígitos: '))

'''

# Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al
# finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma
# función realizada en el ejercicio 2.

'''

def suma_digitos(n):
    copia = n
    suma = 0
    while copia != 0:
        digito = copia % 10
        suma = suma + digito
        copia = copia // 10
    return suma

def suma(n):
    t = 0
    t += n
    return t

preguntar = True
total = 0

while preguntar:
    n = int (input('\r\nIngrese un número: '))
    if n == 0:
        preguntar = False
    else:
        t = suma_digitos(n)
        print (f'La suma de los dígitos de {n} es {t}')
        total += suma(n)
    
t = suma_digitos(total)

print (f'\r\nLa suma total de todos los números es {total}')
print (f'La suma total de los digitos de {total} es {t}')

'''

# Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana
# que lo decida.

'''

def primo(n):
    primo = True
    for i in range (2, 11):
        if n % i == 0:
            if n != i:
                primo = False
    if primo == True:
        return True
    else:
        return False

n = int (input('Ingrese un número y le diré si es primo: '))

if primo(n) == True:
    print (f'{n} es primo.')
else:
    print (f'{n} no es primo.')

'''

# Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el
# número, utilizando para ello una función que calcule la frecuencia.

'''

def frecuencia(n, d):
    copia = n
    f = 0
    while copia != 0:
        digito = copia % 10
        if digito == d:
            f += 1
        copia = copia // 10
    return f
 
n = int (input ('Ingrese un número entero: '))
d = int (input ('Ingrese un dígito: '))
frecuencia = frecuencia(n, d)

print (f'La cantidad de veces que aparece {d} en {n} es {frecuencia}')

'''

# Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue
# mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, 
# según sea necesario.

"""

def suma_digitos(n):
    copia = n
    suma = 0
    while copia != 0:
        digito = copia % 10
        suma = suma + digito
        copia = copia // 10
    return suma

def suma_mayor(n, s, maxx):
    if s > maxx:
        maxx = s
    return n 

'''def menor_10(m):
    menores = []
    if m < 10:  
        menores.append(m)
    return menores
'''
preguntar = True
maxx = -9999

while preguntar:
    n = int (input('Ingrese un número (0 para cortar): '))
    if n == 0:
        preguntar = False
    else:
        suma = suma_digitos(n)
        maxx = suma_mayor(n, suma, maxx)
        
print (n) 

"""

# Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea
# primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la
# cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del
# mayor número ingresado.

'''

def primo(n):

    primo = True
    for i in range (2, 11):
        if n % i == 0:
            if n != i:
                primo = False
    if primo == True:
        return True
    else:
        return False

def suma_digitos(n):
    copia = n
    suma = 0
    while copia != 0:
        digito = copia % 10
        suma = suma + digito
        copia = copia // 10
    return suma

def frecuencia(n, d):
    copia = n
    f = 0
    while copia != 0:
        digito = copia % 10
        if digito == d:
            f += 1
        copia = copia // 10
    return f

def factorial(num):
    f = 1
    for i in range (1, num+1):
        f *= i 
    return f

def num_alto(n, maxx):
    if n > maxx:
        maxx = n
    return maxx

preguntar = True
mayor = -99999

while preguntar:
    num = int (input('\r\nIngrese un número primo: '))
    if primo(num) == False:
        print ('Ha ingresado un número que no es primo. Programa finalizado.')
        preguntar = False
    else:
        print (f'Suma de los digitos: {suma_digitos(num)}')
        frec = int (input ('\r\nIngrese un dígito: '))
        print (f'Cantidad de veces que aparece el {frec} en {num}: {frecuencia(num, frec)}')
        mayor = num_alto(num, mayor)
print (f'\r\nEl número más alto que ingresó es {mayor} y su factorial es {factorial(mayor)}')
        
'''

