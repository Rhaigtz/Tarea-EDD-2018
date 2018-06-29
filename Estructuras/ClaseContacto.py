#Menu del problema
class Contacto:
    def __init__(self, nombre,apellido,telefono,mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail

    def Imprimir(self):
        print("\t Nombre : ", nombre)
        print("\t Apellido : ", apellido)
        print("\t Telefono : ", telefono)
        print("\t mail : ", mail)
