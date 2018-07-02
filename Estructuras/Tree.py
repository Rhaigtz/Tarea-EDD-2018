from ClaseContacto import *
from faker import Faker
from time import time
class Node:
    def __init__(self, value):
        self.data = [value]
        self.parent = None
        self.child = []

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + " : " + str(self.data)
        return "Root: " + str(self.data)

    def _is_leaf(self):
        return len(self.child) == 0

    def _add(self, new_node):
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        for x in range(0, len(self.data)):
            for j in range(x+1, len(self.data)):
                if self.data[j].apellido > self.data[x].apellido:
                    self.data[j], self.data[x] = self.data[x], self.data[j]
        self.child.extend(new_node.child)
        if len(self.child) > 1:
                for x in range(0, len(self.child)):
                    for i in range(0, len(self.child[x].data)):
                        for j in range(x+1, len(self.child[x].data)):
                            if self.child[x].data[j].apellido > self.child[x].data[i].apellido:
                                self.child[x].data[j], self.child[x].data[i] = self.child[x].data[i], self.child[x].data[j]
                         
        if len(self.data) > 2:
            self._split()

    # Encuentra el nodo correcto donde insertar el nuevo nodo
    def _insert(self, new_node):

        # Si es hoja, añade el dato a la hoja y hace un balanceo
        if self._is_leaf():
            self._add(new_node)

        # Si no es hoja, debe encontrar el hijo correcto para descender y hace una inserción recursiva
        elif new_node.data[0].apellido > self.data[-1].apellido:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0].apellido < self.data[i].apellido:
                    self.child[i]._insert(new_node)
                    break

    # Cuando hay 3 items en el nodo, se divide en un nuevo sub-arbol y se añade al padre
    def _split(self):
        left_child = Node(self.data[0])
        right_child = Node(self.data[2])
        if self.child:
        	self.child[0].parent = left_child
        	self.child[1].parent = left_child
        	self.child[2].parent = right_child
        	self.child[3].parent = right_child
        	left_child.child = [self.child[0], self.child[1]]
        	right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]

        # Ahora tenemos un nuevo sub-arbol, y necesitamos añadirlo a su nodo padre
        if self.parent:
        	if self in self.parent.child:
        		self.parent.child.remove(self)
        	self.parent._add(self)
        else:
        	left_child.parent = self
        	right_child.parent = self
	# Busca un item en el arbol y lo retorna siesque lo encuentra, en caso contrario retorna False

    def _find(self, apellido):
    	for i in self.data:
            if apellido in i.apellido:
                return apellido
    	if self._is_leaf():
    		return False
    	elif apellido > self.data[-1].apellido:
    		return self.child[-1]._find(apellido)
    	else:
    		for i in range(len(self.data)):
    			if apellido < self.data[i].apellido:
    				return self.child[i]._find(apellido)

    def _remove(self, apellido):
    	pass

	# Imprime en pre-order
    def _preorder(self):
    	for i in self.data:
            print(i.Imprimir())
    	for child in self.child:
            child._preorder()
        


class Tree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def insert(self, value):
        # Cuando se inserta un valor, siempre se crea un nuevo nodo
        if self.empty():
            self.root = Node(value)
        else:
            self.root._insert(Node(value)) 
            while self.root.parent:
                self.root = self.root.parent
        return True

    def remove(self, apellido):
        return self.root._remove(apellido)

    def find(self, apellido):
        return self.root._find(apellido)

    def pre_order(self):
        self.root._preorder()

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
    lista= Tree()  
    lista.ingresarNContactos(1000)
    tiempo2 = time()
    lista.find(fake.name().split()[1])
    print(time()-tiempo2)


