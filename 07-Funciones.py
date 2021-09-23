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

def suma(n):
    t = 0
    t +=n
    return t

preguntar = True
total = 0

while preguntar:
    n = int (input ('Ingrese un número: '))
    total += suma(n)
    print (total)
    if n == 0:
        preguntar = False 