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

def ingresar_avion(seriales, nombres, modelos):
    """
    Aqui el usuario va a ingresar los datos del avion
    """
    serial = input("Ingrese el serial del avion: ")#el usuario ingresa el serial del avion
    validacion_serial = bool(serial != None) and bool(serial not in seriales) #el username no se encontro en la base de datos
    while (validacion_serial == False or len(serial) != 9 or " " in serial): #Validacion para username
        print("{}Su usuario solo puede contener minusculas y numeros sin ningun espacio{}\n".format(Fore.LIGHTRED_EX, Fore.RESET))
        serial = input("Ingerese el serial nuevamente: ")
        validacion_serial = serial != None and serial not in seriales
    serial = serial.title()

    modelo = input("Ingrese el modelo del avion: ") #el usuario ingresa su nombre
    validacion_modelo = bool(modelo != None) and bool(modelo not in modelos) #el username no se encontro en la base de datos
    while (validacion_modelo == False or len(modelo) > 20 or len(modelo) < 5):
        print("{}Este modelo no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        modelo = input("Ingrese el modelo del avion nuevamente: ")
        validacion_modelo = modelo != None and modelo not in modelos
    modelo = modelo.title() 

    nombre = input("Ingrese el nombre del avion: ") #el usuario ingresa su nombre
    validacion_nombre = bool(modelo != None) and bool(nombre not in nombres) #se valida que el nombre este correcto
    while (validacion_nombre == False or len(nombre) > 12 or len(nombre) < 3):
        print("{}Este nombre no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        nombre = input("Ingrese el nombre del avion nuevamente: ")
        print(nombre not in nombres)
        validacion_nombre = bool(modelo != None) and bool(nombre not in nombres)
    nombre = nombre.title() 

    """ piloto = input("Ingrese el nombre del piloto: ") #el usuario ingresa su nombre
    validacion_piloto = bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})+?', piloto)) #se valida que el nombre este correcto
    while validacion_piloto == False:
        print("{}Este nombre no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        nombre = input("Ingrese el nombre del piloto: ")
        validacion_piloto = bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})+?', piloto))
    piloto = piloto.title()  """
    piloto = ""
    nuevo_avion = Avion(serial, modelo, nombre, piloto)

    with open("Basedatos.txt", "a+") as bd: 
        bd.write(nuevo_avion.para_txt() + "\n") #se agrega el usuario a la base de datos
    
    return nuevo_avion

def datos_usuario():
    """
    Aqui el usuario va a ingresar los datos del avion
    """
    serial = input("Ingrese el serial del avion: ")#el usuario ingresa el serial del avion
    aviones = []
    serial_repetido = True
    while serial_repetido: #se verifica si el serial ya existe
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

def lista_seriales(lista):
    lista_seriales = []
    for x in lista:
        lista_seriales.append(x[1])
    return lista_seriales

def lista_nombres(lista):
    lista_nombres = []
    for x in lista:
        lista_nombres.append(x[0])
    return lista_nombres

def lista_modelos(lista):
    lista_modelos = []
    for x in lista:
        lista_modelos.append(x[0])
    return lista_modelos

def lista_pilotos(lista):
    lista_pilotos = []
    for x in lista:
        if (x.piloto != " " or x.piloto != None or x.piloto != ""):
            lista_pilotos.append(x.piloto)
    return lista_pilotos

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


#def nuevo_avion(avion):


def buscar_avion_serial(serial, hash_table):
    serial = input("Ingrese el serial del avion: ")#el usuario ingresa el serial del avion
    validacion_serial = bool(serial != None)  #el serial no se encontro en la base de datos
    while (validacion_serial == False or len(serial) != 9 or " " in serial): #Validacion para serial
        print("{}El serial solo puede tener letras, numeros sin ningun espacio y 9 caracteres{}\n".format(Fore.LIGHTRED_EX, Fore.RESET))
        serial = input("Ingerese el serial nuevamente: ")
        validacion_serial = bool(serial != None) 
    serial = serial.title()
    avioncito = hash_table.buscar_serial(serial)
    if (avioncito):
        print("El avion de serial {} es el siguiente:".format(serial))
        print(avioncito.encontrado_serial)
    else:
        print("No existe ningun avion con el serial {}".format(serial))


def buscar_avion_modelo(modelo):
    modelo = input("Ingrese el modelo del avion: ") #el usuario ingresa su nombre
    validacion_modelo = bool(modelo != None) #el username no se encontro en la base de datos
    while (validacion_modelo == False or len(modelo) > 20 or len(modelo) < 5):
        print("{}Este modelo no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        modelo = input("Ingrese el modelo del avion nuevamente: ")
        validacion_modelo = bool(modelo != None)
    modelo = modelo.title() 



def buscar_avion_nombre(nombre):
    nombre = input("Ingrese el nombre del avion: ") #el usuario ingresa su nombre
    validacion_nombre = bool(modelo != None) #se valida que el nombre este correcto
    while (validacion_nombre == False or len(nombre) > 12 or len(nombre) < 3):
        print("{}Este nombre no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        nombre = input("Ingrese el nombre del avion nuevamente: ")
        print(nombre not in nombres)
        validacion_nombre = bool(modelo != None)
    nombre = nombre.title() 


#def asignar_piloto():


#def liberar_avion():


#def eliminar_avion():

def main():
    lista = HashTable(3)
    llenar_lista(lista)
    """ print(lista.tabla) 
    avioncito = lista.buscar_serial("B31651041")
    if (avioncito):
        print(avioncito.modelo + " " + avioncito.nombre)"""
    lista.ordenar_indice_nombre()
    lista.ordenar_indice_modelo()
    intro()
    continuar_trabajo = True
    while continuar_trabajo:
        print("""
     Menu        
1) Insertar un nuevo avion
2) Buscar un avion
3) Asignar piloto a un avion libre
4) Liberar un avion
5) Eliminar avion de la flota
6) Salir del programa 
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
            seriales = lista_seriales(lista.indice_modelo)
            print(seriales)
            modelos = lista_modelos(lista.indice_modelo)
            nombres = lista_nombres(lista.indice_nombre)
            avion = ingresar_avion(seriales, nombres, modelos)
            lista.insertar(avion)
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
                print("""
    Menu        
1) Busqueda por serial
2) Busqueda por nombre
3) Busqueda por modelo
""")
            while True:
                try:
                    opcion = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if opcion < 1 or opcion > 3:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            
            if (opcion == 1):
                print(hola)
            
            elif (opcion == 2):
                print(hola)

            elif (opcion == 3):
                print(pepe)
            



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
    sleep(1.25) 

main()


