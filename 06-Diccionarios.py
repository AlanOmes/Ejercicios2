# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su simbolo o un mensaje de aviso si la divisa no esta en el
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
    print ('La divisa no esta.')

'''

# Escribir un programa que pregunte al usuario su nombre, edad, direccion y telefono y lo guarde en un
# diccionario. Despues debe mostrar por pantalla el mensaje <nombre> tiene <edad> anios, vive en <direccion> y
# su numero de telefono es <telefono>.

'''

usuario = {
    'nombre' : input ('¿Cual es tu nombre?: '),
    'edad' : int (input ('¿Cual es tu edad?: ')),
    'direccion' : input ('¿Cual es tu direccion?: '),
    'telefono' : int (input ('¿Cual es tu telefono?: ')), 
}

print ('\r')

print (f'{usuario["nombre"]} tiene {usuario["edad"]} anios, vive en {usuario["direccion"]} y su numero de telefono es {usuario["telefono"]} ')

print ('\r')
print ('---------')
print ('\r')

# Otra forma de hacerlo

n = input ('Ingrese su nombre: ')
e = int (input ('Ingrese su edad: '))
d = input ('Ingrese su direccion: ')
t = int (input ('Ingrese su numero de telefono: '))
u ={
    'nombre' : n,
    'edad' : e,
    'direccion' : d,
    'telefono' : t,
}

print ('\r')

print (f'{u["nombre"]} tiene {u["edad"]} anios, vive en {u["direccion"]} y su numero de telefono es {u["telefono"]}')

'''

# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario
# por una fruta, un numero de kilos y muestre por pantalla el precio de ese numero de kilos de fruta. Si la
# fruta no esta en el diccionario debe mostrar un mensaje informando de ello.

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
        print (f'\r\nEl precio de {c}kg de platanos es ${p} a razon de ${frutas["platano"]} el kilo.') 
    elif f.lower() == 'manzana':
        p = frutas['manzana'] * c
        print (f'\r\nEl precio de {c}kg de manzanas es ${p} a razon de ${frutas["manzana"]} el kilo.')
    elif f.lower() == 'pera':
        p = frutas['pera'] * c
        print (f'\r\nEl precio de {c}kg de peras es ${p} a razon de ${frutas["pera"]} el kilo.')
    elif f.lower() == 'naranja':
        p = frutas['naranja'] * c
        print (f'\r\nEl precio de {c}kg de naranjas es ${p} a razon de ${frutas["naranja"]} el kilo.')
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

# Escribir un programa que almacene el diccionario con los creditos de las asignaturas de un curso 
# {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5} y despues muestre por pantalla los creditos de cada asignatura
# en el formato <asignatura> tiene <creditos> creditos, donde <asignatura> es cada una de las asignaturas del 
# curso, y <creditos> son sus creditos. Al final debe mostrar tambien el numero total de creditos del curso.

'''

notas = {
    'Matematicas' : 6,
    'Fisica' : 4,
    'Quimica' : 5,
}

t = 0

for i in notas:
    t += notas[i]
    print(f'{i} tiene {notas[i]} creditos.')

print ('\r')

print (f'El numero total de creditos del curso es {t}') 

''' 

# Escribir un programa que cree un diccionario vacio y lo vaya llenado con informacion sobre una persona (por
# ejemplo nombre, edad, sexo, telefono, correo electronico, etc.) que se le pida al usuario. Cada vez que se
# aniada un nuevo dato debe imprimirse el contenido del diccionario.

'''

persona = {}
continuar = True

while continuar:
    clave = input('¿Que dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres aniadir mas informacion (Si/No)? ') == "Si"

'''

# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el
# articulo y su precio y aniadir el par al diccionario, hasta que el usuario decida terminar. Despues se debe
# mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

#       Lista de la compra 	

#    Articulo 1 	Precio
#    Articulo 2 	Precio
#    Articulo 3 	Precio
#      …           	…
#     Total 	    Coste

'''

cesta = {}
preguntar = True

while preguntar:
    clave = input ('¿Que producto quieres aniadir a la cesta de compras?: \r\n')
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
# almacenaran en un diccionario donde la clave de cada factura sera el numero de factura y el valor el coste de
# la factura. El programa debe preguntar al usuario si quiere aniadir una nueva factura, pagar una existente o 
# terminar. Si desea aniadir una nueva factura se preguntara por el numero de factura y su coste y se aniadira al
# diccionario. Si se desea pagar una factura se preguntara por el numero de factura y se eliminara del 
# diccionario. Despues de cada operacion el programa debe mostrar por pantalla la cantidad cobrada hasta el 
# momento y la cantidad pendiente de cobro.

'''

facturas = {}
preguntar = True

cobrado = 0
deuda = 0

while preguntar:       
    print ('\r\n1) Aniadir una nueva factura\r\n2) Pagar una factura existente\r\n3) Finalizar')
    opciones = input ('\r\nEscriba el numero de opcion que desee: ')
    if opciones == '1':
        n_factura = input ('\r\nIngrese el numero de la factura: ')
        p_factura = float (input ('Ingrese el valor de la factura: '))
        facturas[n_factura] = p_factura
        deuda += p_factura
        print ('\r\n¡Factura aniadida! Muchas gracias.')
    elif opciones == '2':
        n_factura = input ('\r\nIngrese el numero de la factura: ')
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
        print ('\r\nOpcion inexistente. Por favor, intentelo nuevamente.')
    
    print ('\r\n   FACTuRAS\r\n')
    
    for i in facturas:
        print (f'{i} \t: \t$ {facturas[i]}')
    
    print ('\r')
    print (f'Cantidad recaudada: $ {cobrado}')
    print (f'Cantidad pendiente a cobrar: $ {deuda}')

'''

# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se 
# guardaran en un diccionario en el que la clave de cada cliente sera su NIF, y el valor sera otro diccionario
# con los datos del cliente (nombre, direccion, telefono, correo, preferente), donde preferente tendra el 
# valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opcion del 
# siguiente menu: (1) Aniadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
# (5) Listar clientes preferentes, (6) Terminar. En funcion de la opcion elegida el programa tendra que hacer
# lo siguiente:

# 1) Preguntar los datos del cliente, crear un diccionario con los datos y aniadirlo a la base de datos.
# 2) Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3) Preguntar por el NIF del cliente y mostrar sus datos.
# 4) Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5) Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6) Terminar el programa.

clientes = {}
preferentes = {}

preguntar = True
while preguntar:
    print ('\r\n1) Aniadir cliente\r\n2) Eliminar cliente\r\n3) Mostrar cliente\r\n4) Listar todos los clientes\r\n5) Listar clientes preferentes\r\n6) Terminar')
    opcion = input ('\r\nElija la opcion que desee: ')
    if opcion == '1': # Pide los datos del cliente y lo agrega al diccionario 'clientes' (si el cliente es preferente, tambien lo agrega al diccionario 'preferentes')
        dni = (input('\r\nIngrese el dni del cliente: '))
        info_cliente = input ('Ingrese el nombre completo del cliente: ')
        preferente = input ('¿Es un cliente preferente? (Si/No): ')
        preferente = preferente.capitalize()
        info_cliente = {
        'Nombre' : (f'{info_cliente.title()}'),
        'Documento' : (f'{dni}'),
        'Direccion' : input ('Direccion del cliente: '),
        'Telefono' : input ('Telefono del cliente: '),
        'Correo' : input ('Correo electronico del cliente: '),
        'Preferente' : (f'{preferente}'),
        }
        if preferente == 'Si':
            preferentes[dni] = info_cliente            
        clientes[dni] = info_cliente
        print ('\r\nCliente aniadido correctamente.')
    elif opcion == '2': # Elimina el cliente con el numero de dni
        eliminar = (input ('\r\nIngrese el dni del cliente que quiera eliminar: '))
        if eliminar in clientes:
            del clientes[eliminar] 
            print ('Cliente eliminado con exito. Muchas gracias.')
        else:
            print ('El numero de dni no esta registrado. Por favor, intentelo nuevamente.')        
    elif opcion == '3': 
        cliente = (input('\r\nIngrese el dni del cliente: '))
        if cliente in clientes:
            print('\r')
            for i in clientes[cliente]: 
                c = clientes[cliente] # clientes[cliente] = diccionario de la informacion del cliente (info_cliente)
                print (f'{i}: {c[i]}')
        else:
            print ('El numero de dni no esta registrado. Por favor, intentelo nuevamente.')
    elif opcion == '4':
        print ('\r')
        for i in clientes:
            print ('\r')
            cliente = clientes[i] # clientes[i] diccionario de la informacion del cliente acorde a su dni
            for i in cliente:
                print (f'{i}: {cliente[i]}') # muestra dicho diccionario
    elif opcion == '5':
        print ('\r')
        for i in preferentes:
            print ('\r')
            pref = preferentes[i] # preferentes[i] = diccionario con la informacion del cliente preferente acorde a su dni
            for i in pref:
                print (f'{i}: {pref[i]}')
    elif opcion == '6':
        preguntar = False
        print ('Programa finalizado. Muchas gracias.')






 