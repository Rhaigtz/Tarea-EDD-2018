from ClaseContacto import *
from faker import Faker
from time import time
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None # Añadimos el atributo parent para facilitar la eliminación de un nodo

class ABB:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def _insert(self, value, node):
        if value.apellido < node.value.apellido:
            if node.left == None:
                node.left = Node(value)
                node.left.parent = node
            else:
                self._insert(value, node.left)
        elif value.apellido > node.value.apellido:
            if node.right == None:
                node.right = Node(value)
                node.right.parent = node
            else:
                self._insert(value, node.right)
        else:
            print("Value is already in the Tree")

    def insert(self, value):
        if self.empty():
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _find(self, apellido, node):
        if node == None:
            print("No se encontro el contacto.")
            return None
        elif apellido == node.value.apellido:
            print("El contacto fue encontrado en la estructura.")
            return node
        elif apellido < node.value.apellido and node.left != None:
            return self._find(apellido, node.left)
        elif apellido > node.value.apellido and node.right != None:
            return self._find(apellido, node.right)

    def find(self, apellido):
        if self.empty():
            return None
        else:
            return self._find(apellido, self.root)

    def delete(self, apellido): #Implementar
        if self.empty():
            return None
        return self.delete_node(self.find(apellido))

    def delete_node(self, node):
        if node == None:
            print("El contacto no existe")
            return False
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n): # Return the number of childrens of the node to be deleted
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = node.parent # Get the parent of the node to be deleted
        node_children = number_children(node)

        # Case 1: Deleting a node without childrens
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if node.left != None:
                child = node.left
            else:
                child = node.right

            # Replace the node to be deleted with its child
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            # Change the parent of the child
            child.parent = node_parent
        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = min_value_node(node.right) # Get the inorder successor of the deleted node
            node.value.apellido = successor.value.apellido # Copy the value
            node.value.nombre = successor.value.nombre
            node.value.mail = successor.value.mail
            node.value.telefono=successor.value.telefono
            self.delete_node(successor)

    def in_order(self, node): #Implementar
        if node==None:
            pass
        else:
            self.in_order(node.left)
            print(node.value.Imprimir())
            self.in_order(node.right)

    def post_order(self, node): #Implementar
        if node==None:
            pass
        else:
            self.post_order(node.left)
            self.post_order(node.right)
            print("/t Nombre:  {} Apellido: {} Numero: {} y Email: {} ".format(
                 node.value.nombre, node.value.apellido, node.value.telefono, node.value.mail))

    def pre_order(self, node): #Implementar
        
        if node==None:
            pass
        else:
            print(node.value.Imprimir())
            self.pre_order(node.left)
            self.pre_order(node.right)

    def leaf_number(self): #Implementar
        pass


    def _tree_height(self, current, height):
        if current == None:
            return height
        left_height = self._tree_height(current.left, height+1)
        right_height = self._tree_height(current.right, height+1)
        return max(left_height, right_height)

    def tree_height(self): #Implementar
        if self.empty():
            return 0
        else:
            return self._tree_height(self.root, 0)

    def node_height(self, value): #Implementar
        node = self.root
        height = 0
        if self.find(value):
            height += 1
            while node.value != value:
                if value < node.value:
                    node = node.left
                else:
                    node = node.right
                height += 1
            return height
        return False

    def find_minimum(self): #Implementar
        if self.empty():
            return None
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return current

    def find_maximum(self): #Implementar
        if self.empty():
            return None
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return current

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
        return self.insert(nuevo)

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
            self.insert(nuevo)
        termino = time()
        print(termino-inicio)

if __name__=="__main__":
    fake = Faker()
    lista = ABB()
    lista.ingresarNContactos(1000)
    tiempo1 = time()
    lista.delete(fake.name().split()[1])
    print(time()-tiempo1)
    tiempo2 = time()
    lista.find(fake.name().split()[1])
    print(time()-tiempo2)
