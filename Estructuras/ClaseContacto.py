#Menu del problema
class Contacto:
    def __init__(self, nombre,apellido,telefono,mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail

    def Imprimir(self):
        print("\t Nombre : ", self.nombre)
        print("\t Apellido : ", self.apellido)
        print("\t Telefono : ", self.telefono)
        print("\t mail : ", self.mail)
