#Clase Avion

class Avion:

    def __init__(self, serial, modelo, nombre, piloto):
        self.serial = serial
        self.modelo = modelo
        self.nombre = nombre
        self.piloto = piloto

    def get_serial(self):
        return self.serial

    def get_modelo(self):
        return self.modelo

    def get_nombre(self):
        return self.nombre
    
    def para_txt(self):
        return "{}, {}, {}, {}".format(self.serial, self.modelo, self.nombre, self.piloto)
    