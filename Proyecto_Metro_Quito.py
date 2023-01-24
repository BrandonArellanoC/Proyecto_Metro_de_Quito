from io import open

def bienvenida():
    '''
    Parametro
    --------------
    No ingresa ningun parametro

    Retorna 
    --------------
    No retorna nada
    
    Funcion
    ----------------
    Nos da un membrete de bienvenida
    
    '''
    #Imprime el la cantidad de 56 '*'
    print("*"*56)
    #imprime una bienvenida
    print("Bienvenido al Sistema de Transporte del Metro de Quito ")
    #nos da un aviso
    print("A continuacion te mostraremos las diferentes opciones que puedes hacer ")


def menu():
    '''
    Parametro
    --------------
    No ingresa ningun parametro

    Retorna 
    --------------
    retorna la opcion que se escogio
    
    Funcion
    ----------------
    Nos da un menu  principal para el resto de opciones
    
    '''
    #imprime 20 *
    print("*"*20)
    #nos da la opciones del menu 
    print("Opcion 1: Registrarte ")
    print("Opcion 2: Login ")
    print("Opcion 3: Salir ")
    print("Opcion 4: Ayuda ")
    #se guarda en la variable un entero del ingreso de la opcion del menu  
    opcion = int(input("Ingresa tu opcion :"))
    #retorna la variable que guardo a opcion ingresada por el usuario
    return opcion

def menu_administrativo():
    '''
    Parametro
    --------------
    No ingresa ningun parametro

    Retorna 
    --------------
    retorna la opcion que se escogio
    
    Funcion
    ----------------
    Nos da un menu  para la parte adminsitrativa para el resto de opciones
    
    '''
    print("Opcion 1: Verificación de vin de un vehículo ")
    print("Opcion 2: Validación de códigos para entrada ")
    print("Opcion 3: Verificación de entrada y salida de trenes ")
    print("Opcion 4: Cronometración de viajes por trenes ")
    print("Opcion 5: Asignación de Choferes a los trenes ")
    print("Opcion 6: Salir")
    #se guarda en la variable un entero del ingreso de la opcion del menu  
    opcion = int(input("Ingresa tu opcion :"))
    #retorna la variable que guardo a opcion ingresada por el usuario
    return opcion

def menu_usuario():
    '''
    Parametro
    --------------
    No ingresa ningun parametro

    Retorna 
    --------------
    retorna la opcion que se escogio
    
    Funcion
    ----------------
    Nos da un menu  para el usuario para el resto de opciones
    
    '''
    print("Opcion 1: Ingresar Saldo ")
    print("Opcion 2: conteo de Viajes ")
    print("Opcion 3: salir ")
    #se guarda en la variable un entero del ingreso de la opcion del menu  
    opcion = int(input("Ingresa tu opcion: "))
    #retorna la variable que guardo a opcion ingresada por el usuario
    return opcion


def registro_usuario():
    '''
    Parametro
    --------------
    No ingresa ningun parametro

    Retorna 
    --------------
    No retorna nada
    
    Funcion
    ----------------
    Esta funcion guarda los datos del usuario lo cual se conecta a la base de datos para guardarla y tener el registro
    
    '''
    #en la variable nombre se guarda el ingreso de datos realizados por el usuario 
    nombre = input("Ingrese su nombre: ")
    #en la variable password se guarda la contraseña ingresada por el usario
    password = input("Ingrese su contraseña: ")
    """
    Deberia concectarse a la base y tener el resgistro 
    """
    with open("usuarios.txt","a") as file:
        file.write(nombre + ':' + password + "\n")
    """
    #se abre la base de datos con archivos
    base_usuarios = open("usuarios.txt","w")
    #se guarda los datos de nombre y contraseña 
    base_usuarios.write(nombre + ":" + password)
    #se cierra el archivo 
    base_usuarios.close() 
    """
    #Se imprime que esta exitosamente guardado
    print("Usuario registrado exitosamente!")
    
    

def login():
    '''
    Parametro
    --------------
    No ingresa ningun parametro

    Retorna 
    --------------
    Retorna el tipo de usuario que es: administrativo - usuario
    
    Funcion
    ----------------
    Esta funcion se conecta a la base de datos y se ideantifica si existe el usuario y si ingreso correctamente para poder logiar
    
    '''
    #se guarda el nombre ingresado y el paswword 
    nombre = input("Ingrese su nombre: ")
    password = input("Ingrese su contraseña: ")
    #guarda el tipo de usuario que es
    tipo = input("ingrese 1 si es administrativo,2 si es usuario: ")
    """
    Se conectaria a la base de datos 
    """
    with open("usuarios.txt","r") as file:
        for line in file:
            credenciales = line.strip().split(':')
            credencial_nombre,credencial_password = credenciales[0],credenciales[1]
            if nombre == credencial_nombre and password == credencial_password:
                print("Login correctamente")
                return
            else:
                print("Datos erroneos") 
    #una vez logiado nos diria si es un usuario administrativo o de Usuario
    #ocupa un if si es administrativo 
    if tipo == '1':
        tipo = 'administrativo'
        #Retorna que es de tipo adinistrativo
        return tipo
    #else o caso contratio en tipo nos pone que es de tipo Usuario
    else:
        tipo = 'Usuario'
        #retorna el tipo e usuario
        return tipo

def validacion_codigos(vin_vehiculo):
    '''
    Parametro
    --------------
    Ingresa como parametro el vin de vehiculo 

    Retorna 
    --------------
    Retorna si es validado el vin con un True o False si es invalido
    
    Funcion
    ----------------
    Se hace una comparacion del vin del vehiculo y retorna si es valido o falso

    '''
    #se ocupa un if para la comprobacion del vin
    if vin_vehiculo == 'aaaa':
        #Si es cierto nos ternoa un true
    
        return True
    
    #caso contrario es falso
    else:
        #retorna que es falso
        return False

def validacion_vin(codigos):
    '''
    Parametro
    --------------
    Ingresa como parametro el codigo 

    Retorna 
    --------------
    Retorna si es validado el vin con un True o False si es invalido
    
    Funcion
    ----------------
    Se hace una comparacion del codigo y retorna true si es valido o False si es falso

    '''
    #se ocupa un if para la validacion del codigo
    if codigos == '0000':
        #etorna true si es valido
    
        return True
    #caso contrario retorna false
    else:
        #retorna false
        return False

def entrada_salida_trenes(verificacion):
    '''
    Parametro
    --------------
    Ingresa como parametro la verificacion 

    Retorna 
    --------------
    Retorna si es validado el vin con un True o False si es invalido
    
    Funcion
    ----------------
    Se hace una comparacion del codigo y retorna true si es valido o False si es falso

    '''
    #se ocupa un if para comparar 
    if verificacion != '1':
        #si cumple retorna un true 
        return True
    #caso contrario retorna un false
    else:
        #retona un false
        return False

def ingresar_saldo(saldo):
    '''
    Parametro
    --------------
    Ingresa como parametro el saldo  

    Retorna 
    --------------
    El el saldo añadido
    
    Funcion
    ----------------
    Esta funcion se conectara a la base de datos para actualizar el saldo de la persona

    '''
    #imprime el saldo que se ha ingresado
    print("Se ha ingresado: ",saldo)


def conteo_viajes():

    return print("Numero de viajes han sido: ## ")

def accion(opcion):
    '''
    Parametro
    --------------
    Ingresa como parametro la opcion elejida en el menu principal   

    Retorna 
    --------------
    No rertorna nada
    
    Funcion
    ----------------
    Esta funcion va filtrando de acuerdo a la opcion que se escogio en el menu y va llamando al resto de funciones 
    '''
    
    #ocupa un ciclo repetitivo para que no culmine en lo menus 
    while True:
        #de acuerdo a la opcion escogida se toma la opcion en la que cumple 
        if opcion == 1:
            #llama a la funcion de usuario
            registro_usuario()
            #imprime que el registro se ha culminado 
            print("Registro culminado")
            print("*"*15)
            input("presione para continuar") 
            return accion(menu())
            #break para hacer un cierre forzado
            #break
        #elif para la opcion que sea 2          
        elif opcion == 2:
            #imprime el login
            print("Login")
            #guarda el retorno  del tipo de usuario cuando llama a la funcion
            tipo_usuario = login()
            #imprime que ha ngresado exitosamente
            print("Ha ingresado exitosamente")
            print("*"*15)
            #se hace un if para el usuarioadministrativo y si cumple hace la sentencia 
            if tipo_usuario == 'administrativo':
                #imprime el menu administrativo
                print("Menu administrativo")
                #guarda el retorno de la funcion menu_administrativo
                opcion_administativo = menu_administrativo()
                #ocupa un while para la opciones del menu administrativo
                while opcion_administativo<5:
                    #ocupa un if para filtrar la opcion 
                    if opcion_administativo == 1: 
                        #guarda lo que ingresa el usuario como vin de vehiculo
                        vin_vehiculo = input("Ingrese el vin del vehiculo: ")
                        #manda como parametro el vin_vehiculo y el retorno guarda si es valido o no
                        validacion = validacion_vin(vin_vehiculo)
                        #ocupa un if para la validacion con el tru si es valido y false si no lo es 
                        if validacion == True:
                            print("Validacion Exitosa")
                            #break para cerrar forzadamente
                            break
                        else:
                            print("Error de validacion")
                            break  
                    #ocupa un elfin para la siguientes opciones   
                    elif opcion_administativo == 2:
                        #guarda en la variable el input de lo que se ingreso
                        codigos = input("Ingrese el codigo de pase: ")
                        #se guarda el retorno de la validacion de la funcion y se manda los codigos
                        validacion = validacion_codigos(codigos)
                        #un if para comprobar si es verdadero o falso 
                        if validacion == False:
                            print("Validacion Exitosa")
                            #break para un cierre forzado
                            break
                        else:
                            print("Error de validacion")
                            break
                    #elif para la sigueintes opciones 
                    elif opcion_administativo == 3:
                        
                        print("Si ha ingresado el tren ingrese 1 caso contrario 0")
                        #guarda en la variable el ingreso quesi ha ingresado el tren 
                        verificacion_trenes = input("Ha ingresado el tren : ")
                        #guarda en la variable el retorno de la funcion entrada_salida_trenes y manda como parametro la verificacion_trenes
                        verificacion = entrada_salida_trenes(verificacion_trenes)
                        #ocupa un if para la validacion si es verdadero o falso
                        if verificacion == True:
                            print("Ha entrado exitosamente el tren")
                            #break para el cierre forzado
                            break
                        else:
                            print("Error el tren no ha ingresado")
                            break
                    #elif para la opcion 4
                    elif opcion_administativo == 4:
                        #guarda en la variable la conometracion ingresada por el usario
                        cronometracion = input("Ingrese el timepo que realizo el tren: ")
                        #imprime la cronometracion del tren 
                        print("La cronometracion fue : ",cronometracion)
                        #usa un break para el cierre forzado
                        break
                    #elif para la opcion 5
                    elif opcion_administativo ==5:
                        #guarda en la variable el dato ingresado 
                        tren = input("Ingrese el tren: ")
                        #guarda en la variable el ingreso del nombre del chofer
                        chofer = input("Ingrese al chofer asignado: ")
                        #imprime el tren y el choefer asignado
                        print ("se ha asignado al tren ",tren," con el conductor ",chofer," encargado con esta unidad")
                        #ocupa un break para el cierre forzado 
                        break
                    #elif para la opcion de salir
                    elif opcion_administativo == 6:
                        #break para cierre forzado
                        break
            #en caso contratio entonces es usuario        
            else:
                    print("Menu Usuario")
                    #guarda en la opcion el retorno de la funcion de menu_usuario
                    while True:
                        opcion_usuario = menu_usuario()
                        #ocupa un if para la validacion 
                        if opcion_usuario == 1:
                            #guarda en la variable un float del saldo  
                            saldo = float(input("Ingresa la cantidad de saldo: "))
                            #llama a la funcion ingresar_saldo y manda como parametro el saldo
                            ingresar_saldo(saldo)
                            #break para un cierre forzado
                            return
                        #elif para la opcion 2
                        elif opcion_usuario == 2:
                            #imprime el retorno de la funcion conteo_viajes
                            print("Tus viajes han sido",conteo_viajes())
                            #break para cerre forazdo
                            return
                            #para la opcion salir
                        elif opcion_usuario ==3:
                            #break para el cierre forzado
                            return
            #return al menu principal                
            return accion(menu())
            

        #Elif para la opcion del menu principal 
        elif opcion == 3:

            #print par
            print("Se termino de ejecutar")
            #break para el cierre forzado
            break 
        #elif para la opcion 4 del menu principal 
        elif opcion== 4:
            #imprime las intrucciones del menu principal como ayuda
            print("Las opciones indicadas nos permiten realizar las diferentes acciones",
            "\npara OPCION 1: Nos permite registrarnos en la aplicacion del metro",
            "\nen la OPCION 2: Una vez registrado deberiamos de ingresar con nuestro usuario y contraseña ",
            "\nen la OPCION 3: Cierra el programa  ")
            #en la variable salir ingresa si desea salir con un 1
            salir = int(input("presione 1 para salir: "))
            #if para validar con la vaariable salir 
            if salir == 1:
                #brreak para el cierre forzado
                break



if  __name__ == "__main__":
    #llama a la fncion bienvenida
    bienvenida()
    #llama a la funcion accion y como parametro la funcion menu 
    accion(menu())
