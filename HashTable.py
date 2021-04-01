#Clase Tabla de Hash
from Aviones import Avion


class  HashTable:

    num_elementos = 0
    factor_carga = 0
    tabla = []
    indice_nombre = []
    indice_modelo = []

    def __init__(self, tamano_tabla):
        self.tamano_tabla = tamano_tabla
        self.tabla = [[[]]for element in range(tamano_tabla)]
        self.num_elementos = 0
        self.factor_carga = 0
        """ print(self.tabla) """
    
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
            if (len(self.tabla[posicion]) == x):
                array = []
                self.tabla[posicion].append(array)
            if (len(self.tabla[posicion][x]) == 0):
                self.tabla[posicion][x].append(avion)
                self.llenar_indice_nombre(avion)
                self.llenar_indice_modelo(avion)
                return
            elif (len(self.tabla[posicion][x]) == 1):
                self.tabla[posicion][x].append(avion)
                self.llenar_indice_nombre(avion)
                self.llenar_indice_modelo(avion)
                return
            """elif (len(self.tabla[posicion][0][x]) == 2):
                array = [arra]
                self.tabla[posicion][x].append(avion) 
            
            
            for y in range(2):
                #print(self.tabla[posicion][x][y])
                #print("\n")
                if (self.tabla[posicion][x][y] == None):
                    self.tabla[posicion][x][y] = avion
                    return"""
            if (x == 5):
                print("Ya no hay espacio para añadir este avion")
            
        #self.tabla[posicion].append(avion)
        self.num_elementos +=1

    def ascii_nombre(self, nombre):
        valor = 0
        for x in nombre:
            valor += ord(x)
        return valor

    def llenar_indice_nombre(self, avion):
        tupla = (avion.nombre, avion.serial)
        self.indice_nombre.append(tupla)

    def llenar_indice_modelo(self, avion):
        tupla2 = (avion.modelo, avion.serial)
        self.indice_modelo.append(tupla2)

    """ def myFunc(self):
        return self.indice_nombre['nombre'] """

    def ordenar_indice_nombre(self):
        self.indice_nombre.sort(key=lambda x: self.ascii_nombre(x[0]), reverse=False)
        """ self.indice_nombre.sort(key= nombre) """
        
    def ordenar_indice_modelo(self):
        self.indice_modelo.sort(key=lambda y: self.ascii_nombre(y[0]), reverse=False)
        """ self.indice_nombre.sort(key= nombre) """
        

    def buscar_serial(self, serial):
        posicion = 0
        posicion = self.direccion(serial)
        #valor = None
        for x in range(len(self.tabla[posicion])):
            try:
                for y in range(2):
                    try:
                        if (self.tabla[posicion][x][y].serial == serial):
                            return self.tabla[posicion][x][y]
                        
                    except:
                        print("no se consiguio el avion")
                        return 
            except:
                print("no se consiguio el avion")
                return 
                
    def print_indice_nombre(self):
        for x in self.indice_nombre:
            print(x[0] + " " + x[1])
            print(self.ascii_nombre(x[0]))

    def print_indice_modelo(self):
        for x in self.indice_modelo:
            print(x[0] + " " + x[1])
            print(self.ascii_nombre(x[0]))


    def eliminar(self, serial):
        posicion = 0
        posicion = self.direccion(serial)
        #valor = None
        for x in range(len(self.tabla[posicion])):
            try:
                for y in range(2):
                    try:
                        if (self.tabla[posicion][x][y].serial == serial):
                            return self.tabla[posicion][x][y]
                        
                    except:
                        print("no se consiguio el avion")
                        return 
            except:
                print("no se consiguio el avion")
                return 

        """ posicion = self.direccion(serial)
        if (self.tabla[posicion] != None):
            self.tabla[posicion] = None
            self.num_elementos -=1 """

    def binary_search(arr, low, high, x):#pasar el indice, un 0, el len(tabla) -1 y el valor a buscar
        x = self.ascii_nombre(x)
        if high >= low:

            mid = (high + low) // 2
    
            # If element is present at the middle itself
            if self.ascii_nombre(arr[mid][0]) == x:
                return arr[mid]
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif self.ascii_nombre(arr[mid][0]) > x:
                return binary_search(arr, low, mid - 1, x)
    
            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)
    
            else:
                # Element is not present in the array
                return -1
        




