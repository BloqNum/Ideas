print("Bienvenido al juego: ***Adivina el juego***")
print("En este juego tendra que adivinar un numero en especifico entre el 1 y el 100\nPero solo tendra 10 intentos para poder pegarle. ¡Mucha suerte!")
while 0!=1:
    try:
        import random
        valor=random.randint(1,100)
        for intentos in range(10):
            print(f"Intento {intentos+1}/10\n")
            intento=int(input("Coloque su numero:"))
            if intento==valor:
                print(f"¡Felicidades! Le pegaste en el intento {intentos+1}/10")
                break
            if intento>valor:
                print("Es un numero menor\n")
            if intento<valor:
                print("Es un numero mayor\n")
        if intento!=valor:
            print(f"¡Ups! El numero era {valor}")
        eleccion=input("¿Volver a jugar? ¡Si! o ¡No!:")
        if eleccion.lower()=="no":
            print("Gracias por jugar")
            break 
    except ValueError:
        print("Por favor, coloque un numero")
