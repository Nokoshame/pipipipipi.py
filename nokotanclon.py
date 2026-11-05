def multiplicar(felix):
    for astolfo in range(0, 11):
        print(f"{felix}x{astolfo}={felix*astolfo}")
    return

nombre=input("cual es tu nombre?")

opcion=input(f"{nombre},Elige que programa ejecutar usando las teclas numericas:\n (1)-las tablas de multiplicar \n (2)-contra chida punto py \n (3)-promedios \n (4)")
if opcion=="1":
    felix=int(input(f"{nombre}Elige el numero el cual quieres ver sus tablas de multiplicar"))
    multiplicar(felix)
elif opcion=="2":
    while True:
        password=input(f"{nombre},Escribe tu paswor")
        print("tamal porque no es vaporcito")
        if password=="sonic":
            print(f"felicidades {nombre} bienvenido a el banco de los basados🍷👌😎")
            break
if opcion=="3":
    materiastotales=0
    factosporlosquetepuedenfunarclaro=int(input(f"cuantas materias brochato?"))
    for nokotan in range (factosporlosquetepuedenfunarclaro):
        bashame=float(input(f"escribe la cantidad de la materia {nokotan} brochato"))
        materiastotales=materiastotales+bashame

    print(f"tu promedio de {nokotan+1} materias es:{materiastotales/bashame} meow meow meow meow meow :3")








