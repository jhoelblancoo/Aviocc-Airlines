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
    
    def encontrado_serial(self):
        piloto = ""
        if (self.piloto == "" or self.piloto == " " or self.piloto == None):
            piloto = "No tiene piloto asignado"
        else:
            piloto = self.piloto
        return "Modelo: {}\nNombre: {}\nPiloto: {}".format(self.modelo, self.nombre, piloto)
        
    def encontrado_nombre(self):
        piloto = ""
        if (self.piloto == "" or self.piloto == " " or self.piloto == None):
            piloto = "No tiene piloto asignado"
        else:
            piloto = self.piloto
        return "Serial: {}\nModelo: {}\nPiloto: {}".format(self.serial, self.modelo, piloto)

    def encontrado_modelo(self):
        piloto = ""
        if (self.piloto == "" or self.piloto == " " or self.piloto == None):
            piloto = "No tiene piloto asignado"
        else:
            piloto = self.piloto
        return "Serial: {}\nNombre: {}\nPiloto: {}".format(self.serial, self.nombre, piloto)

    def ascii_nombre(self):
        valor = 0
        nombre = self.nombre
        for x in nombre:
            valor += ord(x)
        return valor
    