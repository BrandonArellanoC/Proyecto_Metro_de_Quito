
def bienvenida():
    print("*"*56)
    print("Bienvenido al Sistema de Transporte del Metro de Quito ")
    print("A continuacion te mostraremos las diferentes opciones que puedes hacer ")


def menu():
    print("*"*20)
    print("Opcion 1: Registrarte ")
    print("Opcion 2: Login ")
    print("Opcion 3: Salir ")
    print("Opcion 4: Ayuda ")
    opcion = int(input("Ingresa tu opcion :"))
    return opcion

def menu_administrativo():
    print("Opcion 1: Verificación de vin de un vehículo ")
    print("Opcion 2: Validación de códigos para entrada ")
    print("Opcion 3: Verificación de entrada y salida de trenes ")
    print("Opcion 4: Cronometración de viajes por trenes ")
    print("Opcion 5: Asignación de Choferes a los trenes ")
    print("Opcion 6: Salir")
    opcion = int(input("Ingresa tu opcion :"))
    return opcion

def menu_usuario():
    print("Opcion 1: Ingresar Saldo ")
    print("Opcion 2: conteo de Viajes ")
    print("Opcion 3: salir ")
    opcion = int(input("Ingresa tu opcion: "))
    return opcion


def registro_usuario():
    nombre = input("Ingrese su nombre: ")
    password = input("Ingrese su contraseña: ")
    

    print("Usuario registrado exitosamente!")

def login():
    nombre = input("Ingrese su nombre: ")
    password = input("Ingrese su contraseña: ")
    tipo = input("ingrese 1 si es administrativo,2 si es usuario: ")
    if tipo == '1':
        tipo = 'administrativo'
        return tipo
    else:
        tipo = 'Usuario'
        return tipo

def validacion_codigos(vin_vehiculo):
    if vin_vehiculo == 'aaaa':
        return True
    else:
        return False

def validacion_vin(codigos):
    if codigos == '0000':
        return True
    else:
        return False

def entrada_salida_trenes(verificacion):
    if verificacion == '1':
        return True
    else:
        return False

def ingresar_saldo(saldo):
    print("Se ha ingresado: ",saldo)

def conteo_viajes():
    return print("Numero de viajes han sido: ## ")

def accion(opcion):

    while True:
        if opcion == 1:
            registro_usuario()
            print("Registro culminado")
            print("*"*15)
            break          
        elif opcion == 2:
            print("Login")
            tipo_usuario = login()
            print("Ha ingresado exitosamente")
            print("*"*15)
            if tipo_usuario == 'administrativo':
                print("Menu administrativo")
                opcion_administativo = menu_administrativo()
                while opcion_administativo<5:
                    
                    if opcion_administativo == 1: 
                        vin_vehiculo = input("Ingrese el vin del vehiculo: ")
                        validacion = validacion_vin(vin_vehiculo)
                        if validacion == True:
                            print("Validacion Exitosa")
                            break
                        else:
                            print("Error de validacion")
                            break    
                    elif opcion_administativo == 2:
                        codigos = input("Ingrese el codigo de pase: ")
                        validacion = validacion_codigos(codigos)
                        if validacion == True:
                            print("Validacion Exitosa")
                            break
                        else:
                            print("Error de validacion")
                            break
                    elif opcion_administativo == 3:
                        print("Si ha ingresado el tren ingrese 1 caso contrario 0")
                        verificacion_trenes = input("Ha ingresado el tren : ")
                        verificacion = entrada_salida_trenes(verificacion_trenes)
                        if verificacion == True:
                            print("Ha entrado exitosamente el tren")
                            break
                        else:
                            print("Error el tren no ha ingresado")
                            break
                    elif opcion_administativo == 4:
                        cronometracion = input("Ingrese el timepo que realizo el tren: ")
                        print("La cronometracion fue : ",cronometracion)
                        break
                    elif opcion_administativo ==5:
                        tren = input("Ingrese el tren: ")
                        chofer = input("Ingrese al chofer asignado: ")
                        print ("se ha asignado al tren ",tren," con el conductor ",chofer," encargado con esta unidad")
                        break
                    elif opcion_administativo == 6:
                        break
                    
            else:
                    print("Menu Usuario")
                    opcion_usuario = menu_usuario()
                    if opcion_usuario == 1:
                        saldo = float(input("Ingresa la cantidad de saldo: "))
                        ingresar_saldo(saldo)
                        break
                    elif opcion_usuario == 2:
                        print("Tus viajes han sido",conteo_viajes())
                        break
                    elif opcion_usuario ==3:
                        break
             


        elif opcion == 3:
            print("Se termino de ejecutar")
            break 
        elif opcion== 4:
            print("Las opciones indicadas nos permiten realizar las diferentes acciones",
            "\npara OPCION 1: Nos permite registrarnos en la aplicacion del metro",
            "\nen la OPCION 2: Una vez registrado deberiamos de ingresar con nuestro usuario y contraseña ",
            "\nen la OPCION 3: Cierra el programa  ")
            salir = int(input("presione 1 para salir: "))
            if salir == 1:
                break


if  __name__ == "__main__":
    bienvenida()
    accion(menu())