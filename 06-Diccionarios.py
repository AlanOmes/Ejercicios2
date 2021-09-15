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

'''

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

'''

# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en 
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

'''

meses = {
    '01' : 'Enero',
    '02' : 'Febrero',
    '03' : 'Marzo',
    '04' : 'Abril',
    '05' : 'Mayo',
    '06' : 'Junio',
    '07' : 'Julio',
    '08' : 'Agosto',
    '09' : 'Septiembre',
    '10' : 'Octubre',
    '11' : 'Noviembre',
    '12' : 'Diciembre',
}

fecha = input ('Escriba una fecha en formato dd/mm/aaaa: ')

d = fecha[:fecha.find('/')]
m1 = fecha[fecha.find('/')+1:]
m = m1[:m1.find('/')]
a = m1[m1.find('/')+1:]

print (f'{d} de {meses[m]} de {a}')

'''

# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del 
# curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

'''

notas = {
    'Matematicas' : 6,
    'Fisica' : 4,
    'Quimica' : 5,
}

t = 0

for i in notas:
    t += notas[i]
    print(f'{i} tiene {notas[i]} créditos.')

print ('\r')

print (f'El número total de créditos del curso es {t}') 

''' 

# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por
# ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se
# añada un nuevo dato debe imprimirse el contenido del diccionario.

datos = ['nombre', 'edad', 'sexo', 'telefono', 'mail']

for i in datos:
    usuario = {
        i : input (f'Ingrese su {i}: '),
    }
print (usuario)  
