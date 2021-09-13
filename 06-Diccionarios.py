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