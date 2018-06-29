
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
      if ot ok:
        self.list[pos].append([key,val]n)
    else:
      self.list[pos] =[]
      self.list[pos].append([key,val])
    
  def get(self,key):
    for e in self.list[hashstr(key,self.size)]:
      if e[0] is key:
        return e[1]
      
  
    
h = hash(10)
h.put("fruta","<img src='http://www.sportlife.es/media/cache/frontend_grande/upload/images/article/16246/article-mejor-tomar-fruta-ayunas-5a4b758d800d3.jpg' width=100/>")
h.put("verdura","<img src='https://biotrendies.com/wp-content/uploads/2016/08/verduras-con-mas-vitamina-c.jpg' width=100/>")
h.put("chatarra","<img src='https://metalurgia.cloudingenium.com/wp-content/uploads/sites/12/2012/08/Transformacion-Puebla-Compra-de-chatarra-de-aluminio1.jpg' width=100/>")
h.put("chatarra","<img src='http://culturizando.com/wp-content/uploads/2016/11/thumb_600x0_Comida-rapida.png' width=100/>")
h.put("mesa","<img src='https://www.ikea.com/es/es/images/products/morbylanga-mesa__0533580_PE648686_S4.JPG' width=100/>")
h.put("same","<img src='http://www.corporate-eye.com/main/wp-content/uploads/2011/09/same-stripe.jpg' width=100/>")
h.put("mase","<img src='http://www.gstatic.com/tv/thumb/persons/914646/914646_v9_ba.jpg' width=100/>")

print(h.get("fruta")+"<br>")
print(h.get("verdura")+"<br>")
print(h.get("chatarra")+"<br>")
print(h.get("mesa")+"<br>")
print(h.get("same")+"<br>")
print(h.get("mase")+"<br>")
