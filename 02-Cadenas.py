# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por
# pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

'''

nombre = input ('Escriba su nombre: ')
numero = int (input ('Escriba un número entero: '))

for i in range (numero):
    print (nombre)

'''

# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla
# el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras
# mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede 
# introducir su nombre combinando mayúsculas y minúsculas como quiera.

'''

nombre = input ('Ingrese su nombre completo: ')

print (nombre.lower())
print (nombre.upper())
print (nombre.title())

'''

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
# introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
# mayúsculas y <n> es el número de letras que tienen el nombre.

'''

nombre = input ('Ingrese su nombre: ')

print (f'{nombre.upper()} tiene {len(nombre)} letras.')

'''

# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el 
# código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa 
# que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el 
# prefijo y la extensión.

'''

numero = input ('Ingrese el número de teléfono: ')

print (f'El número de teléfono es {numero[4:-3]}')

'''

# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la
# frase invertida.

'''

frase = input ('Escriba una frase: ')

print (frase[::-1])

'''

# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después 
# muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

'''

frase = input('Escriba una frase: ')
vocal = input ('Escriba una vocal: ')

print (frase.replace(vocal, vocal.upper()))

'''    

# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
# correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es

'''

mail = input ('Ingrese su correo electrónico: ')
cortado = mail.split(" ")[-1].split("@")[0]

print (f'{cortado}@ceu.es')

cor = mail[:mail.find('@')] # Otra forma de resolverlo

print (f'{cor}@ceu.es')

'''

# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre
# por pantalla el número de euros y el número de céntimos del precio introducido.

'''

precio = input ('Introduzca el precio del producto con dos decimales: ')
e = precio[:precio.find('.')] # Los dos puntos al principio para que vaya desde el principio hasta el punto marcado
c = precio[precio.find('.')+1:] # Los dos puntos a lo último para que vaya desde el punto marcado hasta el final (el '+1' sirve para que imprima un caracter después del punto marcado)

print (f'{e} euros y {c} céntimos.')

'''

# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por
# pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el
# mes se introduzcan con un solo carácter.

'''

fecha = input ('Escriba su fecha de nacimiento: ')

d = fecha[:fecha.find('/')]
m1 = fecha[fecha.find('/')+1:]
m = m1[:m1.find('/')]
a = m1[m1.find('/')+1:]

print (f'Día: {d}') 
print (f'Mes: {m}')
print (f'Año: {a}')

'''

# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por
# comas, y muestre por pantalla cada uno de los productos en una línea distinta.

cesta = input ('Escriba, separados por coma, los productos que compró: ')

lista = cesta.split(', ')

print ('LISTA DE COMPRAS\r\n')

for i in lista:
    print (i)
