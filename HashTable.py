#Clase Tabla de Hash
from Aviones import Avion


class  HashTable:

    num_elementos = 0
    factor_carga = 0
    tabla = []

    def __init__(self, tamano_tabla):
        self.tamano_tabla = tamano_tabla
        self.tabla = [[[None, None]for element in range(6)]for element in range(tamano_tabla)]
        self.num_elementos = 0
        self.factor_carga = 0
        print(self.tabla)
    
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
        """ if (len(self.tabla[posicion]) == 0):
            self.tabla[posicion].append(avion)
        elif (len(self.tabla[posicion]) == 1):
             
        elif (len(self.tabla[posicion]) > 1):
            array = [avion]
            self.tabla[posicion][2] = array
         """
        for x in range(6):
            for y in range(2):
                #print(self.tabla[posicion][x][y])
                #print("\n")
                if (self.tabla[posicion][x][y] == None):
                    self.tabla[posicion][x][y] = avion
                    return
            if (x == 5):
                print("Ya no hay espacio para añadir este avion")
            
        #self.tabla[posicion].append(avion)
        self.num_elementos +=1
        

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
        




