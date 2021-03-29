#Clase Tabla de Hash
from Aviones import Avion


class  HashTable:

    num_elementos = 0
    factor_carga = 0
    tabla = []

    def __init__(self, tamano_tabla):
        self.tamano_tabla = tamano_tabla
        self.tabla = [[] for element in range(tamano_tabla)]
        self.num_elementos = 0
        self.factor_carga = 0
    
    def direccion(self, clave):
        p = 0
        letra = ord(clave[0])
        d = int(clave[1:])
        d += letra
        p = int(d % self.tamano_tabla)
        return p

    def insertar(self, avion):
        posicion = 0
        posicion = self.direccion(avion.serial)
        self.tabla[posicion].append(avion)
        self.num_elementos +=1
        self.factor_carga = self.num_elementos / self.tamano_tabla
        if (self.factor_carga > 0.5):
            print("el factor de carga aumento")
        

    def buscar_serial(self, serial):
        posicion = 0
        posicion = self.direccion(serial)
        valor = self.tabla[posicion]
        return valor

    def eliminar(self, serial):
        posicion = self.direccion(serial)
        if (self.tabla[posicion] != None):
            self.tabla[posicion] = None
            self.num_elementos -=1
        




