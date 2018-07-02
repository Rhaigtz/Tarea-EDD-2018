from ClaseContacto import *
from time import time
from faker import Faker
#El nodo almacena la clase contacto
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class List:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

    def borrar(self,apellido):
        if self.head.data.apellido == apellido:
            self.head = self.head.next_node
            return apellido
        aux = self.head
        while aux.next_node:
            if aux.next_node.data.apellido == apellido:
                aux.next_node = aux.next_node.next_node
                print("Contacto Eliminado con exito")
                break
            aux = aux.next_node


    def buscar(self,apellido):
        i = 1
        aux = self.head
        while aux:
            if aux.data.apellido == apellido:
                print("El contacto fue encontrado en el nodo numero {} ".format(i))
                return True
                break
            else:
                aux = aux.next_node
                i+=1
                if aux is None:
                    return False
                    break

    def sortedInsert(self, contact):
        if self.buscar(contact.apellido) is True:
            return True
        else:
            NodoContacto = Node(contact)
            # Special case for the empty linked list
            if self.head is None:
                NodoContacto.next_node = self.head
                self.head = NodoContacto

        # Special case for head at end
            elif self.head.data.apellido >= contact.apellido:
                NodoContacto.next_node = self.head
                self.head = NodoContacto

            else:
            # Locate the node before the point of insertion
                current = self.head
                while(current.next_node is not None and current.next_node.data.apellido < contact.apellido):
                    current = current.next_node

                NodoContacto.next_node = current.next_node
                current.next_node = NodoContacto

    def print_list(self):
        if self.empty():
             print("Lista de contactos vacia")
        else:
            temp = self.head
            i = 1
            while temp:
                print("El Nodo numero {} contiene el contacto".format(i))
                print(temp.data.Imprimir())
                temp = temp.next_node
                i += 1

    def agregarContacto(self):
        print("Agregar nombre: ")
        nombre = input()
        print("Agregar apellido: ")
        apellido = input()
        print("Agregar telefono: ")
        telefono = input()
        print("Agregar email: ")
        email = input()
        nuevo = Contacto(nombre, apellido, telefono, email)
        return self.sortedInsert(nuevo)


    def ingresarNContactos(self, n):
        from random import randint
        fake = Faker()
        inicio = time()
        for i in range(0, n):
            x = fake.name()
            y = x.split()
            email = fake.email()
            telefono = str(randint(11111111, 99999999))
            nuevo = Contacto(y[0], y[1], telefono, email)
            self.sortedInsert(nuevo)
        termino = time()
        print(termino-inicio)
        
if __name__ == "__main__":
    fake = Faker()
    lista= List()  
    lista.ingresarNContactos(1000)
    tiempo1 = time()
    lista.borrar(fake.name().split()[1])
    print(time()-tiempo1)
    tiempo2 = time()
    lista.buscar(fake.name().split()[1])
    print(time()-tiempo2)
