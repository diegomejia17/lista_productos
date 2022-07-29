#importaciones.
from Producto import *

#variables globales 
lista_de_productos = []

def acccion_usuario():
    contador  = 0
    while (contador >=0 and contador <=4) :
        system("clear")
        imprimir_menu()
        contador  = int( input(" "))

        if contador == 1 :
            agregar_productos(lista_de_productos)
            input("")
        elif contador ==2:
            borrar_productos(lista_de_productos)
            input("")
        elif contador == 3 :
            mostrar_lista(lista_de_productos)
            input("")
        elif  contador == 4:
            pagar(lista_de_productos)
            input("")
        


def imprimir_menu():
    print("\t \t Bienvenido \nSeleccione una opcion")
    print("1- Agregar productos\n2- Borrar productos\n3- Mostrar la lista de compra\n4- pagar\n5-salir")


def main ():
    acccion_usuario()
    




# llamado de la funcion pricipal.
main()