from ClaseContacto import *
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
            pass
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
                break
            else:
                aux = aux.next_node
                i+=1
                if aux is None:
                    print("El contacto no se encuentra registrado en la lista")
                    break

    def sortedInsert(self, contact):
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

    def borrarContacto(self):
        print("Ingrese el Apellido del contacto que desea eliminar:")
        apellido = input()
if __name__ == "__main__":

    contacto = Contacto("Nicolas", "Opazo", 4319413, "dasads")
    contacto2 = Contacto("Luis", "Apaza", 41242112, "dasdsa")
    contacto3 = Contacto("rodrigo", "villanueva", 4321431, "fdsafadfa")
    contacto5 = Contacto("dassjkkj", "Gonzales", 214414, "faskjfs")
    contacto6 = Contacto("Bastian", "Navarro", 243894231, "dsakjdsa")
    lista=List()
    lista.sortedInsert(contacto)
    lista.sortedInsert(contacto2)
    lista.borrar("Opazo")
