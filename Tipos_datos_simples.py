# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

'''

print ('¡Hola mundo!')

'''

# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el 
# contenido de la variable.

'''

saludo = '¡Hola Mundo!'

print (saludo)

'''

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
# introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya 
# introducido.

'''

nombre = input('Ingrese su nombre: ')

print (f'¡Hola {nombre}!')

'''

# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2)^2
#                                                                                                  ---
#                                                                                                  2.5

'''

a = 3 + 2
b = 2 * 5

print ((a / b) * (a / b))

'''

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después
# debe mostrar por pantalla la paga que le corresponde.

'''

cant_horas = float (input ('Ingrese la cantidad de horas trabajadas: '))
precio_hora = float (input ('Ingrese cuánto cobra por hora: '))
cobro_total = cant_horas * precio_hora

print (f'El monto que debe cobrar es de ${cobro_total}.')

'''

# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada 
# de la siguiente forma: n (n + 1)
#                        ---------
#                            2

'''

num = int (input ('Ingrese un número entero positivo:'))

for num in range (1, num+1):
    a = num * (num + 1)
    suma = a // 2
print (suma) 

'''

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa 
# corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

'''

peso = int (input ('Ingrese su peso: '))
altura = float (input ('Ingrese su altura en metros: '))
imc = peso / (altura ** 2)
imc = round ( imc, 2)

print (f'Tu índice de masa corpral es {imc} ')

'''

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un 
# cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el 
# cociente y el resto de la división entera respectivamente.

'''

n = int (input ('Ingrese un número entero: '))
m = int (input ('Ingrese otro número entero: '))

c = n // m
r = n % m

print (f'{n} entre {m} da un cociente de {c} y un resto de {r}. ')

'''

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.

'''

inversion = int (input ('Ingrese la cantidad a invertir: $'))
interes = int (input ('Ingrese el porcentaje de interés anual: '))
años = int (input ('Ingrese el número de años que va a invertir: '))

total_obtenido = inversion * (interes / 100 + 1) ** años
total_obtenido = round (total_obtenido, 2)

print (f'El total a obtener es: ${total_obtenido}')

'''

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
# la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y
# muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
# programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del
# paquete que será enviado.

'''

cant_payasos = int (input ('Ingrese la cantidad de payasos: '))
cant_muñecas = int (input ('Ingrese la cantidad de muñecas: '))

peso_payaso = 112
peso_muñeca = 75

peso = (cant_payasos * peso_payaso) + (cant_muñecas * peso_muñeca)

print (f'Payasos vendidos: {cant_payasos}\r\nMuñecas vendidas: {cant_muñecas}\r\nPeso del paquete: {peso}g')

'''

# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros
# debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de 
# ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros 
# tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

'''

ahorros = int (input ('Ingrese la cantidad de dinero que va a ingresar: $'))

uno = (ahorros * 4) / 100 + ahorros
uno = round (uno, 2)
dos = (uno * 4) / 100 + uno
dos = round (dos, 2)
tres = (dos * 4) / 100 + dos
tres = round (tres, 2)

print (f'Ahorros después de un año: ${uno}\r\nAhorros después de dos años: ${dos}\r\nAhorros después de tres años: ${tres}')

'''

# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el
# programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca
# y el coste final total.

cant_pan = int (input ('Ingrese la cantidad de panes que no son del día vendidos: '))

descuento = 3.49 - (60 * 3.49) / 100
descuento = round (descuento, 2) 
coste_total = cant_pan * descuento

print (f'Precio de barra de pan: 3.49€\r\nPrecio con descuento: {descuento}€\r\nCoste total: {coste_total}€')