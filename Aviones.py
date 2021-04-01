#Clase Avion

class Avion:

    def __init__(self, serial, modelo, nombre, piloto):
        self.serial = serial
        self.modelo = modelo
        self.nombre = nombre
        self.piloto = piloto

    def get_serial(self):
        return self.serial
    
    def para_txt(self):
        return "{}, {}, {}, {}".format(self.serial, self.modelo, self.nombre, self.piloto)

    def ascii_nombre(self):
        valor = 0
        nombre = self.nombre
        for x in nombre:
            valor += ord(x)
        return valor
    