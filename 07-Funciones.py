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

f = 0

def factorial(num):
    for i in range (1, num +1):
        f *= i
        print (f)        

num = 5
factorial(num)
    
