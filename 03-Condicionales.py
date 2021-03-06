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

'''

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

'''

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta
# formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo
# B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo 
# que le corresponde.

'''

nombre = input ('Escriba su nombre: ')
sexo = input ('Escriba su sexo (F/M): ')

nombre = nombre.capitalize()
sexo = sexo.capitalize()

if nombre[0] <= 'M':
    if sexo[0] == 'F':
        print ('Pertenece al grupo A.')
    else:
        print ('Pertenece al grupo B.')
if nombre[0] >= 'N':
    if sexo[0] == 'M':
        print ('Pertenece al grupo A.')
    else:
        print ('Pertenece al grupo B.')
    
'''

# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

'''

#      Renta                  Tipo impositivo

# Menos de 10000€ 	               5%
# Entre 10000€ y 20000€ 	      15%
# Entre 20000€ y 35000€ 	      20%
# Entre 35000€ y 60000€ 	      30%
# Más de 60000€ 	              45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le
# corresponde.

r = float (input ('Escriba su renta anual: '))

if r < 10000:
    print ('Tramo impositivo correspondiente: 5%')
elif r >= 10000 and r < 20000:
    print ('Tramo impositivo correspondiente: 15%')
elif r >= 20000 and r < 35000:
    print ('Tramo impositivo correspondiente: 20%')
elif r >= 35000 and r < 60000:
    print ('Tramo impositivo correspondiente: 30%')
else:
    print ('Tramo impositivo correspondiente: 45%')

'''

# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener 
# en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que
# pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras
# mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La
# cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

#    Nivel           	Puntuación

#  Inaceptable 	          0.0
#  Aceptable 	          0.4
#  Meritorio 	          0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la 
# cantidad de dinero que recibirá el usuario.

'''

p = float (input ('Escriba su puntuación: '))
d = p * 2400

if p < 0.4:
    print ('Nivel: Inaceptable.')
elif p >= 0.4:
    print (f'Nivel: Aceptable\r\nDinero: {d}€')
elif p >= 0.6:
    print (f'Nivel: Meritorio\r\nDinero: {d}€')

'''

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de
# forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario
# la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
# si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

'''

edad = int (input('Escriba su edad: '))

if edad < 4:
    print ('Entrada gratuita.')
elif edad >= 4 and edad < 18:
    print ('Entrada: 5€')
else:
    print ('Entrada: 10€')

'''

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para 
# cada tipo de pizza aparecen a continuación.

#  -  Ingredientes vegetarianos: Pimiento y tofu.
#  -  Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
# respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un
# ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por 
# pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

'''

print ('\r\n¡Bienvenido a Bella Napoli!\n')
print ('1) Pizza no vegetariana\r\n2) Pizza vegetariana\r\n')

pedido = input ('Por favor, ingrese el número correspondiente a lo que quiera pedir:\r\n')

print('\r')

if pedido == '1':
    print ('\rPIZZA NO VEGETARIANA\r\n')
    print ('1) Peperoni\r\n2) Jamón\r\n3) Salmón\r\n')
    i = input ('Ingrese el número correspondiente al ingrediente que quiera agregar (el tomate y la muzzarella ya están añadidos): \r\n')
    print ('\r\n¡Excelente! Muchas gracias.')
    if i == '1':
        print ('\r\nPedido solicitado: Pizza no vegetariana con peperoni.')
    elif i == '2':
        print ('\r\nPedido solicitado: Pizza no vegetariana con jamón.')
    elif i == '3':
        print ('\r\nPedido solicitado: Pizza no vegetariana con salmón.')
    else:
        print ('¡Opción incorrecta! Por favor, inténtelo nuevamente.')
elif pedido == '2':
    print ('\rPIZZA VEGETARIANA\r\n')
    print ('1) Pimiento\r\n2) Tofu')
    i = input ('Ingrese el número correspondiente al ingrediente que quiera agregar (el tomate y la muzzarella ya están añadidos: \r\n')
    print ('\r\n¡Excelente! Muchas gracias.')
    if i == '1':
        print ('\r\nPedido solicitado: Pizza vegetariana con pimiento.')
    elif i == '2':
        print ('\r\nPedido solicitado: Pizza vegetariana con tofu.')
    else:
        print ('¡Opción incorrecta! Por favor, inténtelo nuevamente.')
else:
    print ('¡Opción incorrecta! Por favor, inténtelo nuevamente.')

'''