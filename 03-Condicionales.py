# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

'''

edad = int (input ('Escriba su edad: '))

if edad >= 18:
    print ('Es mayor de edad.')
else:
    print ('Es menor de edad.')

'''

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por
# la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en
# la variable sin tener en cuenta mayúsculas y minúsculas.

'''

c = 'b22eadc1'

cc = input ('Por favor, ingrese la contraseña: ')

if c == c.lower():
    print ('Contraseña correcta.')
else:
    print ('Contraseña incorrecta.')

'''

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es
# cero el programa debe mostrar un error.

'''

n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))

if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)

'''

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

'''

num = int (input ('Por favor, ingrese un número: '))

if num % 2 == 0:
    print ('El número es par.')
else:
    print ('El número es impar.')

''' 

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores 
# a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre 
# por pantalla si el usuario tiene que tributar o no.

e = int (input ('Ingrese su edad: '))
i = int (input ('Escriba sus ingresos mensuales: '))

if e >= 16 and i >= 1000:
    print ('Usted puede tributar.')
elif e >= 16:
    print ('Para tributar, su ingreso mensual debe ser igual o superior a 1000€')
elif i >= 1000:
    print ('Para tributar debe ser mayor de 16 años.')
else:
    print ('Para tributar debe ser mayor de 16 años y su ingreso mensual debe ser igual o superior a 1000€')
