from ClaseContacto import *
from faker import Faker
from time import time
outputdebug = False


def debug(msg):
    if outputdebug:
        print (msg)


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def empty(self):
        return self.node == None

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node

        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key.apellido < tree.key.apellido:
            self.node.left.insert(key)

        elif key.apellido > tree.key.apellido:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key.apellido) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key.apellido) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, apellido):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None:
            if self.node.key.apellido == apellido:
                debug("Deleting ... " + str(apellido))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  # sanity check
                        debug("Found replacement for " + str(key.apellido) +
                              " -> " + str(replacement))
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key.apellido)

                self.rebalance()
                return
            elif apellido < self.node.key.apellido:
                self.node.left.delete(apellido)
            elif apellido > self.node.key.apellido:
                self.node.right.delete(apellido)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node != None:  # just a sanity check

            while node.left != None:
                debug("LS: traversing: " + str(node.key.apellido))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def pre_order(self, nodo):  # Implementar

            if nodo == None:
                pass
            else:
                self.pre_order(nodo.left.node)
                print("Nombre:  {} Apellido: {} Numero: {} y Email: {} ".format(
                    nodo.key.nombre, nodo.key.apellido, nodo.key.telefono, nodo.key.mail))
                self.pre_order(nodo.right.node)

    def find(self, apellido):
        if self.empty():
            return None
        else:
            return self._find(apellido, self.node)

    def _find(self, apellido, node):
        if node == None:
            return None
        elif apellido == node.key.apellido:
            print(node.key.apellido)
        elif apellido < node.key.apellido and node.left != None:
            return self._find(apellido, node.left.node)
        elif apellido > node.key.apellido and node.right != None:
            return self._find(apellido, node.right.node)


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

if __name__ == "__main__":

    fake = Faker()
    lista= AVLTree()  
    lista.ingresarNContactos(1000)
    tiempo1 = time()
    lista.delete(fake.name().split()[1])
    print(time()-tiempo1)
    tiempo2 = time()
    lista.find(fake.name().split()[1])
    print(time()-tiempo2)
