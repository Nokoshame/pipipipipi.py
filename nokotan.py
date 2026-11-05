def multiplicar(felix):
    for astolfo in range(0, 11):
        print(f"{felix}x{astolfo}={felix*astolfo}")
    return

nombre=input("cual es tu nombre?")

opcion=input(
    f"{nombre},Elige que programa ejecutar usando las teclas numericas:\n (1)-las tablas de multiplicar \n (2)-contra chida punto py \n (3)-suma de rupias  "
)
if opcion=="1":
    felix=int(input(f"{nombre}Elige el numero el cual quieres ver sus tablas de multiplicar"))
    multiplicar(felix)
elif opcion=="2":
    while True:
        password=input(f"{nombre},Escribe tu paswor")
        print("tamal porque no es vaporcito")
        if password=="sonic":
            print("felicidades shinji")
            break
if opcion=="3":
    rupiastotales=0
    factosporlosquetepuedenfunarclaro=int(input(f"cuantas semanas brochato?"))
    for nokotan in range (factosporlosquetepuedenfunarclaro):
        bashame=float(input(f"escribe la cantidad de rupias en semana {nokotan} brochato"))
        rupiastotales=rupiastotales+bashame

print(f"tus rupias totales en {nokotan+1} semanas son:{rupiastotales} meow meow meow meow meow :3")








