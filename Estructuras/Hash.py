from ClaseContacto import *
from faker import Faker
from time import time

def str2num(key):
  return sum([ord(c) for c in key])

def hashstr(key,size):
  return str2num(key)%size


class hash:
  def __init__(self,size):
    self.list = [None]*size
    self.size= size

  def put(self,key,val):
    pos = hashstr(key,self.size)
    if self.list[pos] is not None:
      print("collision "+key+"<br>")
      ok = False
      for t in self.list[pos]:
        if t[0] is key:
          t[1] = val
          ok = True
      if not ok:
        self.list[pos].append([key,val])
    else:
      self.list[pos] =[]
      self.list[pos].append([key,val])

  def get(self,key):
    for e in self.list[hashstr(key,self.size)]:
      if e[0] is key:
        print(time()-x)
        return e[1]

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
            self.put(nuevo.apellido,nuevo)
        termino = time()
        print(termino-inicio)

if __name__ == "__main__":

  fake = Faker() 
  h = hash(150)
  h.ingresarNContactos(10)
  x = time()
  h.get(fake.name().split()[1])
  print(time()-x)
