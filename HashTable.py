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
        for x in range(8):
            #Abuelo 1, Padre 3, Hijos 6
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
            if (x == 7):
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
                        return None
            except:
                return None

    def print_tabla(self, tabla):
        for x in range(len(tabla)):
            try:
                if (len(tabla[x]) > 1):
                    print("[ {} , {} ]".format(tabla[x][0].get_serial(), tabla[x][1].get_serial()))
                else:
                    print("[ {} ]".format(tabla[x][0].get_serial()))
                    
            except:
                return None
                
    def eliminar_serial(self, serial):
        posicion = 0
        posicion = self.direccion(serial)
        buscar = True
        #Con este print se comprueba como se elimina el avion print(self.print_tabla(self.tabla[posicion]))
        #valor = None
        largo = len(self.tabla[posicion])
        for x in range(len(self.tabla[posicion])):
            if (buscar):
                try:
                    for y in range(2):
                        try:
                            if (y == 0):
                                if (self.tabla[posicion][x][y].serial == serial):
                                    print("Se elimino al avion de serial {}:".format(serial))
                                    print(self.tabla[posicion][x][y].encontrado_serial())
                                    self.tabla[posicion][x].pop(0)
                                    if (len(self.tabla[posicion][x]) == 0): 
                                        self.tabla[posicion].pop(x)
                                        #Con este print se comprueba como se elimina el avion print(self.print_tabla(self.tabla[posicion]))
                                    buscar = False
                                    break
                            else:
                                if (buscar and self.tabla[posicion][x][y].serial == serial):
                                    print("Se elimino al avion de serial {}:".format(serial))
                                    print(self.tabla[posicion][x][y].encontrado_serial())
                                    self.tabla[posicion][x].pop()
                                    buscar = False
                            
                        except:
                            return None
                except:
                    return None
            elif(not buscar):
                prev = x-1
                for y in range(2):
                    if (len(self.tabla[posicion][x]) == 1):
                        self.tabla[posicion][prev].append(self.tabla[posicion][x][y])
                        self.tabla[posicion].pop(x)
                        break
                    elif (y == 0):
                        self.tabla[posicion][prev].append(self.tabla[posicion][x][y])
                        self.tabla[posicion][x].pop(0)
                        break

            if (x == largo-1):
                print("")
                #Con este print se comprueba como se elimina el avion print(self.print_tabla(self.tabla[posicion]))

                    
                
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
                        return 
            except:
                return 

        """ posicion = self.direccion(serial)
        if (self.tabla[posicion] != None):
            self.tabla[posicion] = None
            self.num_elementos -=1 """

    def binary_search(self, lista, low, high, ascii_clave, string_clave):#pasar el indice, un 0, el len(tabla) -1 y el valor a buscar
        try:
            if high >= low:

                mid = (high + low) // 2
        
                #Si el elemento que se busca esta en la mitad de la lista
                if self.ascii_nombre(lista[mid][0]) == ascii_clave:
                    if (lista[mid][0] == string_clave):
                        return lista[mid]
                    else:
                        return self.binary_search(lista, low, mid, ascii_clave, string_clave) #puede ser mid -1
        
                # Si el elemento es menor que el mid
                #estara presenta en el lado izquierdo de la lista
                elif self.ascii_nombre(lista[mid][0]) > ascii_clave:
                    return self.binary_search(lista, low, mid - 1, ascii_clave, string_clave)
        
                #Entonces el elemento estara presente en el lado derecho de la lista
                else:
                    return self.binary_search(lista, mid + 1, high, ascii_clave, string_clave)
        
            else:
                # El elemento no esta en el array
                return -1
        except:
            return -1
    
    def listar_piloto(self, serial, piloto):
        posicion = 0
        posicion = self.direccion(serial)
        #valor = None
        for x in range(len(self.tabla[posicion])):
            try:
                for y in range(2):
                    try:
                        if (self.tabla[posicion][x][y].serial == serial):
                            if(self.tabla[posicion][x][y].piloto == "" or self.tabla[posicion][x][y].piloto == " " or self.tabla[posicion][x][y].piloto == None):
                                self.tabla[posicion][x][y].piloto = piloto
                                print("Se asigno a {} como piloto del avion {}".format(piloto, self.tabla[posicion][x][y].modelo))
                                return True
                            else:
                                print("Ya el piloto {} tiene asignado el avion {}".format(self.tabla[posicion][x][y].piloto, self.tabla[posicion][x][y].modelo))
                                return False
                        
                    except:
                        return False
            except:
                return False

    def quitar_piloto(self, serial):
        posicion = 0
        posicion = self.direccion(serial)
        #valor = None
        for x in range(len(self.tabla[posicion])):
            try:
                for y in range(2):
                    try:
                        if (self.tabla[posicion][x][y].serial == serial):
                            if(self.tabla[posicion][x][y].piloto != "" and self.tabla[posicion][x][y].piloto != " " and self.tabla[posicion][x][y].piloto != None):
                                pilot = self.tabla[posicion][x][y].piloto
                                self.tabla[posicion][x][y].piloto = ""
                                print("Se elimino a {} como piloto del avion {}".format(pilot, self.tabla[posicion][x][y].modelo))
                                return True
                            else:
                                print("El avion {} no tiene ningun piloto asignado".format(self.tabla[posicion][x][y].modelo))
                                return False
                        
                    except:
                        return False
            except:
                return False
        




