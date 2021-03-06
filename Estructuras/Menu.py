from ListaC import *
from ArbolBinario import *
from AVL2 import *
from Tree import *
from faker import Faker
from time import time
from Hash import *
class Menu:
    def __init__(self):
        self.cont = 0


    def Inicio(self,lista,abb,avl,tree):
        lista = List()
        abb = ABB()
        avl = AVLTree()
        tree = Tree()
        print("Bienvenido a su lista de contactos \nIngrese la lista que desee implementar en sus Contactos")
        print("1. Lista de Contacto")
        print("2. Arbol Binario")
        print("3. AVL")
        print("4. 2_3 Tree")
        op=int(input("Ingrese opcion: "))
        if op==1:
            self.Lista()
        elif op==2:
            self.ArbolBinario()
        elif op==3:
            self.AVLtree()
        elif op==4:
            self.Trees()
        elif op==5:
            self.Hashing()
        else:
            print("A ingresado una opción no valida, por favor vuelva a ingresar opcion")
            self.Inicio()

    def Lista(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("4. Buscar Contacto")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            lista.agregarContacto()
            self.cont +=1
            self.Lista()

        elif op==2:
            print("Ingrese el Apellido del contacto que desea eliminar:")
            apellido = input()
            lista.borrar(apellido)
            self.cont -=1
            self.Lista()

        elif op==3:
            lista.print_list()
            self.Lista()

        elif op==4:
            print("Ingrese el Apellido del contacto a buscar")
            apellido = input()
            lista.buscar(apellido)
            self.Lista()
        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.Inicio()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.Lista()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.Lista()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.Lista()

    def ArbolBinario(self):
        print("Ha ingresado el arbol binario de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("4. Buscar Contacto")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            abb.agregarContacto()
            self.cont +=1
            self.ArbolBinario()

        elif op==2:
            print("Ingrese el Apellido del contacto que desea eliminar:")
            apellido = input()
            abb.delete(apellido)
            self.cont -=1
            self.ArbolBinario()

        elif op==3:
            abb.in_order(abb.root)
            self.ArbolBinario()

        elif op == 4:
            print("Ingrese el Apellido del contacto a buscar")
            apellido = input()
            abb.find(apellido)
            self.ArbolBinario()
        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.ArbolBinario()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.ArbolBinario()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.ArbolBinario()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.ArbolBinario()


    def AVLtree(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("4. Buscar Contacto")

        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            avl.agregarContacto()
            self.cont +=1
            self.AVLtree()

        elif op==2:
            print("Ingrese el Apellido del contacto que desea eliminar:")
            apellido = input()
            avl.delete(apellido)
            self.cont -=1
            self.AVLtree()

        elif op==3:
            avl.pre_order(avl.node)
            self.AVLtree()
        
        elif op == 4:
            print("Ingrese el Apellido del contacto a buscar")
            apellido = input()
            avl.find(apellido)
            self.Lista()

        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.AVLtree()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.AVLtree()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.AVLtree()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.AVLtree()
    
    def Trees(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("3. Desplegar Contactos")
        print("4. Buscar Contacto")
        print("0. Volver al Menu Anterior")

        op = int(input("Ingrese opcion: "))
        if op == 1:
            tree.agregarContacto()
            self.cont += 1
            self.Trees()

        elif op == 3:
            tree.pre_order()
            self.Trees()
        elif op == 4:
            print("Ingrese el Apellido del contacto a buscar")
            apellido = input()
            tree.find(apellido)
            self.Trees()
        elif op == 0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.Trees()

            elif aux == 2:
                print("Reiniciar Menu de Lista\n")
                self.Trees()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.Trees()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.Trees()

    def hash(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("4. Buscar Contacto")
        print("0. Volver al Menu Anterior")

        op = int(input("Ingrese opcion: "))
        if op == 1:
            h.agregarContacto()
            self.cont += 1
            self.hash()
        elif op == 4:
            print("Ingrese el Apellido del contacto a buscar")
            apellido = input()
            h.get(apellido)
            self.hash()
        elif op == 0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.hash()

            elif aux == 2:
                print("Reiniciar Menu de Lista\n")
                self.hash()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.hash()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.hash()

   
if __name__ == "__main__":
    menu = Menu()
    h = hash(100)
    lista = List()
    abb = ABB()
    avl = AVLTree()
    tree = Tree()
    menu.Inicio(lista,abb,avl,tree)

