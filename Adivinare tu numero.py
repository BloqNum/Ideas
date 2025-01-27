print("En este programa vos podes pensar en un numero del 1 al 100 y yo intentare adivinarlo\nUna vez mostrado el numero, deberas ingresar si es [Mayor], [Menor] o [Correcto]")
valor2=1
valor3=100
try:
    decision=input("¿Ya pensaste?[Escriba Si]:")
    if decision.lower()=="si":
        import random
        valor=random.randint(1,100)
        while 0<1:
            pista=input(f"¿Tu numero es {valor}?:")
            if pista.lower()=="mayor":
                valor2=valor
                valor=random.randint(valor,valor3)
            if pista.lower()=="menor":
                valor3=valor
                valor=random.randint(valor2,valor)
            if pista.lower()=="correcto":
                print("¡Felicidades por mi!")
                break
    else:
        print("\nAhora te quedas sin juego por gil")
except Exception as loco:
    print(loco)
#hay un bug, en el cual cuando alguien repite el mismo numero diciendo que es menor mas de una vez, el programa cuando le digas que es mayor te va a poner como limite el numero anterior, osea que te quedara ej:(27,27)

        
            
