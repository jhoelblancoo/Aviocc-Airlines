from Aviones import Avion
from HashTable import HashTable
from time import sleep
from colorama import Fore
import re




def intro():
    """
    Muestra el titulo inicial del programa
    """
    sleep(1)
    print("\n")
    print(" "*70 + Fore.LIGHTBLACK_EX + "Bienvenido a\n" + Fore.RESET)
    sleep(1.25)
    print("\n" + Fore.RED + " "*70 + "AVIOCC")
    sleep(1.25)
    print(" "*75 + "AIRLINES\n" + Fore.RESET)
    sleep(1.25)
    #print(" "*71 + Fore.LIGHTBLACK_EX + "Presenta\n" + Fore.RESET)
    #sleep(1.25)
    #print(" "*66 + Fore.LIGHTBLUE_EX + "███ " + "BATTLESHIP" + " ███" + Fore.RESET)
    #sleep(1)

def datos_usuario():
    """
    Aqui el usuario va a ingresar sus datos (username, nombre, edad y genero)
    """
    serial = input("Ingrese el serial del avion: ")#el usuario ingresa su username
    aviones = []
    serial_repetido = True
    while serial_repetido: #se verifica si el username ya jugo antes
        with open("BaseDatos.txt", "r") as bd:
            datos = bd.readlines()
        for x in datos:
            avion = x[:-1].split(',') #si el username esta en la base de datos no necesita ingresar sus datos
            aviones.append(avion[0])
            #se procede a extraer los datos del username guardado y copiarlos 
            if serial in aviones:
                print("Un avion con este serial ya existe en la base de datos\n")
                """sleep(2)
                serial = avion[0]
                modelo = avion[1].split(" ")
                modelo = modelo[1].title()
                nombre = avion[2].split(" ")
                piloto = avion[3].split(" ")
                with open("Basedatos.txt", "r") as db: 
                    lineas = db.readlines()
                with open("Basedatos.txt", "w") as db: #se reescribe la lista en la base de datos sin el usuario actual  
                    for linea in lineas:
                        if serial not in linea:
                            db.write(linea) 
                with open("Basedatos.txt", "a") as bd: #se agrega a la base de datos el usuario actual que ya ha jugado antes, se mantienen todos sus datos pasados
                    bd.write("{}, {}, {}, {}, {}, {}\n".format(username, nombre, edad, genero, puntaje, disparos_efectuados))
                return Usuario(username, nombre, edad, genero, puntaje, disparos_efectuados)
                username_repetido = False"""
        else:
            validacion_serial = serial #el username no se encontro en la base de datos
            while validacion_serial == False or len(serial) > 9 or " " in serial: #Validacion para username
                print("{}Su usuario solo puede contener minusculas y numeros sin ningun espacio{}\n".format(Fore.LIGHTRED_EX, Fore.RESET))
                serial = input("Ingerese el serial nuevamente: ")
                validacion_serial = serial != None
            serial = serial.title()

            modelo = input("Ingrese el modelo del avion: ") #el usuario ingresa su nombre
            validacion_modelo = bool(modelo != None) #se valida que el nombre este correcto
            while validacion_modelo == False:
                print("{}Este modleo no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
                nombre = input("Ingrese el modelo del avion: ")
                validacion_modelo = bool(modelo != None)
            modelo = modelo.title() 

            nombre = input("Ingrese el nombre del avion: ") #el usuario ingresa su nombre
            validacion_nombre = bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})+?', nombre)) #se valida que el nombre este correcto
            while validacion_nombre == False:
                print("{}Este nombre no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
                nombre = input("Ingrese el nombre del avion: ")
                validacion_nombre = bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})+?', nombre))
            nombre = nombre.title() 

            piloto = input("Ingrese el nombre del piloto: ") #el usuario ingresa su nombre
            validacion_piloto = bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})+?', piloto)) #se valida que el nombre este correcto
            while validacion_piloto == False:
                print("{}Este nombre no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
                nombre = input("Ingrese el nombre del piloto: ")
                validacion_piloto = bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})+?', piloto))
            piloto = piloto.title() 

            nuevo_avion = Avion(serial, modelo, nombre, piloto)
            with open("Basedatos.txt", "a+") as bd: 
                bd.write(nuevo_avion.para_txt() + "\n") #se agrega el usuario a la base de datos
            serial_repetido = False
            return nuevo_avion


def llenar_lista(hash_table):
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        y = x[:-1].split(",")
        serial = y[0]
        modelo = y[1]
        modelo = modelo[1:]
        nombre = y[2]
        nombre = nombre[1:]
        piloto = y[3]
        piloto = piloto[1:]
        avion = Avion(serial, modelo, nombre, piloto)
        hash_table.insertar(avion)
    #cont = 0
    """ #print(hash_table.tabla)
    for x in hash_table.tabla: #se almacenaran solo los 10 primeros usuarios en otra lista y se mostraran
        if (len(x) > 0):
            if (len(x) > 1):
                for y in x:
                    #print(Fore.LIGHTMAGENTA_EX + y.serial + " " + y.modelo + " " + y.nombre + Fore.RESET)
            #else:
                #print(Fore.LIGHTMAGENTA_EX + x[0].serial + " " + x[0].modelo + " " + x[0].nombre + Fore.RESET)
        cont += 1 """
    print("\n")

#def hash():
#def hash(self, key):
	#hashsum = 0
	# For each character in the key
	#for idx, c in enumerate(key):
		# Add (index + length of key) ^ (current char code)
		#hashsum += (idx + len(key)) ** ord(c)
		# Perform modulus to keep hashsum in range [0, self.capacity - 1]
		#hashsum = hashsum % self.capacity
	#return hashsum


#def nuevo_avion(avion):


#def buscar_avion_serial(serial):


def buscar_avion_modelo(modelo):
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        y = x[:-1].split(",")
        modelo = y[1]
        modelo = modelo[1:]
        hash_table.buscar_modelo(modelo)

def buscar_avion_nombre(nombre):
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        y = x[:-1].split(",")
        nombre = y[2]
        nombre = nombre[1:]
        hash_table.buscar_nombre(nombre)

#def asignar_piloto():


#def liberar_avion():


#def eliminar_avion():

def main():
    lista = HashTable(3)
    """print(lista.tabla[0])
    lista.insertar(avion1)
    print(len(lista.tabla[5]))
    datos_usuario()"""
    llenar_lista(lista)
    print(lista.tabla)
    avioncito = lista.buscar_serial("B31651041")
    if (avioncito):
        print(avioncito.modelo + " " + avioncito.nombre)
    """ intro()
    continuar_trabajo = True
    while continuar_trabajo:
        print("""
    """ Menu        
1) Insertar un nuevo avion
2) Buscar un avion
3) Asignar piloto a un avion libre
4) Liberar un avion
5) Eliminar avion de la flota
6) Salir del programa """
""")
        while True:
            try:
                elegir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                if elegir < 1 or elegir > 6:
                    raise  ValueError
                break
            except ValueError:
                print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))

        if elegir == 1:
            print("\nInsertar avion")
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_trabajo = True
            else: continuar_trabajo = False
        
        elif elegir == 2:
            print("\nBuscar avion")
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_trabajo = True
            else: continuar_trabajo = False
        
        elif elegir == 3:
            print("\nAsignar piloto")
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_trabajo = True
            else: continuar_trabajo = False
        
        elif elegir == 4:
            print("\nLiberar avion")
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_trabajo = True
            else: continuar_trabajo = False
        
        elif elegir == 5:
            print("\nEliminar avion")
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_trabajo = True
            else: continuar_trabajo = False

        elif elegir == 6:
            continuar_trabajo = False

    print("\nTe deseamos un feliz dia, gracias por utilizar nuestro servicios \n")
    sleep(1)
    print(" "*66 + Fore.RED + "███ " + "Aviocc Airlines" + " ███" + Fore.RESET + "\n")
    sleep(1.25) """

main()


