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





def cuadrado(l):
    l_c = []
    for i in l:
        c = i ** 2
        l_c.append(c)
    return l_c

l = [1, 2, 3, 4, 5]

print (cuadrado(l))



# Juli



def suma(a, b): 
    r = a + b # 2
    return r # 3

s =  suma(2, 2) # 1

if s % 2 == 0: # 4 
    print (f'{s} es par') # 5
else: # 4
    print (f'{s} es impar.') # 5

