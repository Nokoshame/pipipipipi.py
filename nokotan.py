

def multiplicar(numerodetablademultiplicar):
    for i in range(0, 11):
        print(f"la tabla del {numerodetablademultiplicar} {numerodetablademultiplicar}x{i}={numerodetablademultiplicar*i} ")
    return
def multiplicarbait(numerodebait):
    for i in range(0, 67676766666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666667):
        print(f"{numerodebait}x{i}=si ")
        return

nombre=input("cual es tu nombre?")

opcion=input(f"{nombre},Elige que programa ejecutar usando las teclas numericas:\n (1)-el banco de los basados(caso 1) \n (2)-promedios finales(caso 2) \n (3)-adivina el numero version tsundere (caso 3) \n (4)-las tablas de multiplicar(caso 4) \n (5)-el gran cohetito de alfredo larin(caso 5) \n (6)-el ahorro del bienestar (caso 6) \n (7)-peso de las maletas por el que te pueden funar,claro (caso 7) \n (67) ¡LAS EPICAS TABLAS DE MULTIPLICAR MUY BIEN OPTIMIZADAS!")
#CASO 1.
# Un sistema de seguridad de un cajero permite al usuario ingresar su NIP. Si se equivoca, el  programa debe advertirle
# y volver a pedirlo hasta que introduzca la clave correcta

if opcion=="1":
    while True:
     password=input(f"{nombre},Escribe tu paswor")
     print("tamal porque no es vaporcito")

     if password=="sonic":
         print(f"felicidades {nombre} bienvenido a el banco de los basados🍷👌😎")
         break
#CASO 2 Un profesor necesita calcular el promedio final de un estudiante. El programa le pregunta
#primero cuántas materias cursó y, mediante un bucle, le pide la calificación de cada una
#para acumularlas, calcular el promedio e imprimir si aprobó o reprobó con base en una
#ondicional
if opcion=="2":
    promedio=0
    cantidadmaterias=int(input(f"cuantas materias brochato?"))
    for i in range(cantidadmaterias):
        calificacion_materias=float(input(f"escribe la calificacion de la materia {i+1} brochato"))
        promedio=promedio+calificacion_materias

    print(f"{nombre} tu promedio de {i+1} materias es:{promedio/cantidadmaterias} meow meow meow meow meow :3")

#caso 3 La computadora "piensa" un número fijo (o se le asigna uno). El usuario debe intentar
#adivinarlo. En cada intento, si falla, el programa le indica si el número secreto es mayor o
#menor, repitiendo el proceso hasta que lo adivine, contando cuántos intentos le toma
if opcion=="3":
    numero_intentos=4
    numero=67
    while numero_intentos>0:
        print("BAKA! Adivina el numero en el que estoy pensando.... NO TE ESTOY PREGUNTANDO TE ESTOY DANDO UNA ORDEN MPHHH")
        intentos=int(input(f"adivina.... el numero"))

        if intentos==67:
            print(f"mphhhh! adivinaste el numero {nombre}...... ")
            print("BAKA")
            break

        elif intentos>numero:
            numero_intentos=numero_intentos-1
            print(f"el numero que pusiste es mayor {nombre} OmO,Te quedan {numero_intentos} intentos restantes....")

        elif intentos<numero:
            numero_intentos=numero_intentos-1
            print(f"El numero que pusiste es menor {nombre},Te quedan {numero_intentos} intentos restantes....")
#le pide al estudiante que ingrese un número entero mediante input. El programa debe
#generar y mostrar en pantalla su tabla de multiplicar del 1 al 10 utilizando un bucle
if opcion=="4":
    numero=int(input("Escribe el numero que quieres multiplicar Om0"))
    multiplicar(numero)
    print("\n miau miau miau miau")
#desde aca me dio flojera poner nota de que caso es que asi que como los casos estan en orden porfa asuma cual caso es cual
if opcion=="5":
    import time
    delay=0.6
    numerocontador=int(input(f"{nombre} ¡EL COHETE DE ALFREDO LARIN ESTA A PUNTO DE DESPEGAR! \n ESCRIBE EL NUMERO DE TIEMPO EL CUAL DEBE DURAR EL CONTADOR"))
    for i in range(1,numerocontador+1):
        time.sleep(delay)
        print(f"el cohete despega en {i}...")
    print("despegue!")


if opcion=="6":
    ahorrototal=0
    print("tu meta es ahorrar 67 pesos")
    while ahorrototal<67:
        dinerosemanal=int(input(f"{nombre} escribe la cantidad de dinero que ahorraste OwO"))
        ahorrototal=ahorrototal+dinerosemanal
        faltante=67-ahorrototal
        if faltante>0:
            print(f"tu cantidad ahorrada es:{ahorrototal} te faltan {faltante} pesos para llegar a la meta")
        else:
            print(f"tu cantidad ahorrada es:{ahorrototal} llegaste a la meta metosa!")


if opcion == "7":
    cantidadmaletas=0
    cantidadmaletaspesoextra=0
    pesomaletas=0
    pesomaletastotal=0
    print("Bienvenido a el vuelo 11 de American Airlines!\n tu te encargas de contar el peso de las maletas y detectar peso maximo ")
    while pesomaletastotal<25:
        pesomaletas=int(input("escribe el peso de la maleta"))
        pesomaletastotal=pesomaletastotal+pesomaletas
        cantidadmaletas=cantidadmaletas+1
        print(f"peso de las maletas{pesomaletastotal}\n cantidad maletas{cantidadmaletas}")
    if pesomaletas>25:
        cantidadmaletaspesoextra=cantidadmaletaspesoextra+1
        print(f"peso de las maletas{pesomaletastotal}la cantidad de maletas que han excedido el peso es {cantidadmaletaspesoextra}  ")
        pesomaletas=int(input("escribe el peso de la maleta"))
        pesomaletastotal=pesomaletastotal+pesomaletas






if opcion=="67":
   kabuto=int(input("escribe el numero que quieres multiplicar :3"))
   multiplicarbait(kabuto)









	














