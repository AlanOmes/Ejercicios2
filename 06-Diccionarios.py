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

'''

persona = {}
continuar = True

while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

'''

# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el
# artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe
# mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

#       Lista de la compra 	

#    Artículo 1 	Precio
#    Artículo 2 	Precio
#    Artículo 3 	Precio
#      …           	…
#     Total 	    Coste

'''

cesta = {}
preguntar = True

while preguntar:
    clave = input ('¿Qué producto quieres añadir a la cesta de compras?: \r\n')
    valor = float (input (f'Precio de {clave}: '))
    cesta[clave] = valor
    p = input ('¿Quieres seguir agregando productos a la cesta de compras? (Si/No): ')
    if p.upper() == 'NO':
        preguntar = False

print ('\r\n')
print ('       LISTA DE COMPRAS')
print ('\r')

t = 0

for i in cesta:
    print (f'{i} \t\t\t${cesta[i]}')
    t += cesta[i]

print ('...\t\t\t...')
print (f'Total\t\t\t{t}')

'''

# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se 
# almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de
# la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o 
# terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al
# diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del 
# diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el 
# momento y la cantidad pendiente de cobro.

'''

facturas = {}
preguntar = True

cobrado = 0
deuda = 0

while preguntar:       
    print ('\r\n1) Añadir una nueva factura\r\n2) Pagar una factura existente\r\n3) Finalizar')
    opciones = input ('\r\nEscriba el número de opción que desee: ')
    if opciones == '1':
        n_factura = input ('\r\nIngrese el número de la factura: ')
        p_factura = float (input ('Ingrese el valor de la factura: '))
        facturas[n_factura] = p_factura
        deuda += p_factura
        print ('\r\n¡Factura añadida! Muchas gracias.')
    elif opciones == '2':
        n_factura = input ('\r\nIngrese el número de la factura: ')
        for i in facturas:
            if i == n_factura:
                pagar = True
                cobrado += facturas[n_factura]
                deuda -= facturas[n_factura]
        if pagar == True:
                del facturas[n_factura]
                print ('\r\n¡Pago realizado! Muchas gracias.')
    elif opciones == '3':                           
        preguntar = False
        print ('\r\n¡Programa finalizado! Muchas gracias.')
    else:
        print ('\r\nOpción inexistente. Por favor, inténtelo nuevamente.')
    
    print ('\r\n   FACTURAS\r\n')
    
    for i in facturas:
        print (f'{i} \t: \t$ {facturas[i]}')
    
    print ('\r')
    print (f'Cantidad recaudada: $ {cobrado}')
    print (f'Cantidad pendiente a cobrar: $ {deuda}')

'''

# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se 
# guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario
# con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el 
# valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del 
# siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
# (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer
# lo siguiente:

# 1) Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# 2) Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3) Preguntar por el NIF del cliente y mostrar sus datos.
# 4) Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5) Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6) Terminar el programa.

