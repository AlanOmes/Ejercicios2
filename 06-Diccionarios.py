# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el
# diccionario.

'''

divisa = {
    'Euro' : '€',
    'Dolar' : '$',
    'Yen' : '¥'
}

p = input ('Escribe una divisa: ')

if p.title() in divisa:
    print (divisa[p.title()])
else:
    print ('La divisa no está.')

'''

# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
# diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y
# su número de teléfono es <teléfono>.

'''

usuario = {
    'nombre' : input ('¿Cuál es tu nombre?: '),
    'edad' : int (input ('¿Cuál es tu edad?: ')),
    'direccion' : input ('¿Cuál es tu dirección?: '),
    'telefono' : int (input ('¿Cuál es tu teléfono?: ')), 
}

print ('\r')

print (f'{usuario["nombre"]} tiene {usuario["edad"]} años, vive en {usuario["direccion"]} y su número de teléfono es {usuario["telefono"]} ')

print ('\r')
print ('---------')
print ('\r')

# Otra forma de hacerlo

n = input ('Ingrese su nombre: ')
e = int (input ('Ingrese su edad: '))
d = input ('Ingrese su dirección: ')
t = int (input ('Ingrese su número de teléfono: '))
u ={
    'nombre' : n,
    'edad' : e,
    'direccion' : d,
    'telefono' : t,
}

print ('\r')

print (f'{u["nombre"]} tiene {u["edad"]} años, vive en {u["direccion"]} y su número de teléfono es {u["telefono"]}')

'''

# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario
# por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la
# fruta no está en el diccionario debe mostrar un mensaje informando de ello.

frutas = {
    'platano' : 1.35,
    'manzana' : 0.80,
    'pera' : 0.85,
    'naranja' : 0.70,
}

f = input ('Ingrese la fruta que desee comprar: ')


if f.lower() in frutas:
    c = float (input ('Ingrese la cantidad de kilos que quiera llevar: '))
    if f.lower() == 'platano':
        p = frutas['platano'] * c
        print (f'\r\nEl precio de {c}kg de platanos es ${p} a razón de ${frutas["platano"]} el kilo.') 
    elif f.lower() == 'manzana':
        p = frutas['manzana'] * c
        print (f'\r\nEl precio de {c}kg de manzanas es ${p} a razón de ${frutas["manzana"]} el kilo.')
    elif f.lower() == 'pera':
        p = frutas['pera'] * c
        print (f'\r\nEl precio de {c}kg de peras es ${p} a razón de ${frutas["pera"]} el kilo.')
    elif f.lower() == 'naranja':
        p = frutas['naranja'] * c
        print (f'\r\nEl precio de {c}kg de naranjas es ${p} a razón de ${frutas["naranja"]} el kilo.')
else:
    print ('\r\nLo siento, no disponemos de esa fruta.')