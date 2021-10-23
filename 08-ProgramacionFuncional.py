# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una
# tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de 
# las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de
# la cesta y devolver el precio final de la cesta.

def aplicar_descuento(precio, porcentaje):
    cantidadADescontar = (porcentaje * precio) / 100
    precioFinal = precio - cantidadADescontar
    return precioFinal

def aplicar_iva(precio, iva):
    cantidadADescontar = (iva * precio) / 100
    precioFinal = precio + cantidadADescontar
    return precioFinal

def aplicar_iva_o_descuentos(precios_y_porcentajes, funcion):
    for i in precios_y_porcentajes:
        precioFinal = funcion(i, precios_y_porcentajes[i])
        return precioFinal

lista_de_precios = {
    100 : 10,
    200 : 20,
    300 : 30,
}

print (aplicar_iva_o_descuentos(lista_de_precios, aplicar_iva()))






