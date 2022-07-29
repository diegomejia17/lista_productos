
from os import system
import math

def agregar_productos(lista_de_productos):
    producto = []
    producto.append(input("ingrese el nombre del producto:\n"))
    producto.append(float(input("ingrese el precio del producto:\n")))
    lista_de_productos.append(producto)
    print("producto agregado")

def borrar_productos(lista_de_productos):
    contador = 1
    #condicional que evalua que no este vacia la lista
    if len(lista_de_productos) > 0 :
        print("Seleccione el producto que desea eliminar.")

        #Recorrido de la lista de productos, para poder mostrar el nombre.
        for producto in lista_de_productos :
            print(str(contador) +"- "+ producto[0] )
            contador = contador +1 
        indice_producto_seleccionado = int(input("\n")) -1

        #manejo de exepcion debido a que el usuario puede ingresar un indice que no esta contendo en la lista.
        try:
            lista_de_productos.pop(indice_producto_seleccionado)
        except IndexError:
            print("producto seleccionado no es valido.")
        else:
            print("producto eliminado.")
    else:
        print("lista vacia.")

    
def mostrar_lista(lista_de_productos):
    contador = 1
    print("Lista de productos")

    #Recorrido de la lista de productos, para mostrarlos en pantalla
    for producto in lista_de_productos :
        print(str(contador) +"- "+ producto[0] + " $" + str(producto[1]))
        contador = contador +1 
    
def pagar(lista_de_productos):
    
    numero_productos_lista = len(lista_de_productos)
    descuento = 0
    porcentaje_desc1 = 0.10
    porcentaje_desc2 = 0.15
    cantidad_producto_desc1 = 5
    cantidad_producto_desc2 = 10
    total_minimo_desc1 = 100
    total_minimo_desc2 = 200
    total_pagar = 0

    #Recorrido de la lista de productos, para calcular el costo de todos los productos 
    for producto in lista_de_productos:
        total_pagar = total_pagar+producto[1]

    #condicional que evalua si la cantidad de productos es > 5 y el total es 100
    if numero_productos_lista > cantidad_producto_desc1 and math.isclose(total_minimo_desc1, total_pagar):
        descuento = (porcentaje_desc1 * total_pagar)

    #condicional que evalua si la cantidad de productos es > 10 y el total es > 200
    if numero_productos_lista > cantidad_producto_desc2 and total_pagar > total_minimo_desc2:
        descuento = (porcentaje_desc2 * total_pagar)

    total_pagar = total_pagar - descuento
    
      
    print("cantidad de productos: " + str(numero_productos_lista)) 
    print("Descuento: " + str(descuento))
    print("Total de la compra $" + str(total_pagar))
