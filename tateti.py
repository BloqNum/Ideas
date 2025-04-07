total=[[[],[],[]],[[],[],[]],[[],[],[]]]
empate=0
try:
    for i in total:
        print(i)
    while 0<1:
        if total[0].count("X")==3 or total[1].count("X")==3 or total[2].count("X")==3 or total[0][0]=="X" and total[1][0]=="X" and total[2][0]=="X" or total[0][1]=="X" and total[1][1]=="X" and total[2][1]=="X" or total[0][2]=="X" and total[1][2]=="X" and total[1][2]=="X" or total[0][0]=="X" and total[1][1]=="X" and total[2][2]=="X" or total[0][2]=="X" and total[1][1]=="X" and total[2][0]=="X":
            print("Gano X".upper())
            input("Presione Enter para salir")
            break
        if total[0].count("O")==3 or total[1].count("O")==3 or total[2].count("O")==3 or total[0][0]=="O" and total[1][0]=="O" and total[2][0]=="O" or total[0][1]=="O" and total[1][1]=="O" and total[2][1]=="O" or total[0][2]=="O" and total[1][2]=="O" and total[1][2]=="O" or total[0][0]=="O" and total[1][1]=="O" and total[2][2]=="O" or total[0][2]=="O" and total[1][1]=="O" and total[2][0]=="O":
            print("Gano O".upper())
            input("Presione Enter para salir")
            break
        empate=total[0].count("X") + total[0].count("O") + total[1].count("X") + total[1].count("O") + total[2].count("X") + total[2].count("O")
        if empate==9:
            print("Hubo un empate".upper())
            input("Presione Enter para salir")
            break
        print("\nAhora va X".upper())
        y=int(input("Seleccione del 1 al 3 para su casilla en orden vertical:"))
        x=int(input("Seleccione del 1 al 3 para su casilla en orden horizontal:"))
        if total[y-1][x-1]=="O":
            print("No puedes sobreescribir")
        else:
            total[y-1][x-1]="X"
            for i in total:
                print(i)
        if total[0].count("X")==3 or total[1].count("X")==3 or total[2].count("X")==3 or total[0][0]=="X" and total[1][0]=="X" and total[2][0]=="X" or total[0][1]=="X" and total[1][1]=="X" and total[2][1]=="X" or total[0][2]=="X" and total[1][2]=="X" and total[1][2]=="X" or total[0][0]=="X" and total[1][1]=="X" and total[2][2]=="X" or total[0][2]=="X" and total[1][1]=="X" and total[2][0]=="X":
            print("Gano X".upper())
            input("Presione Enter para salir")
            break
        if total[0].count("O")==3 or total[1].count("O")==3 or total[2].count("O")==3 or total[0][0]=="O" and total[1][0]=="O" and total[2][0]=="O" or total[0][1]=="O" and total[1][1]=="O" and total[2][1]=="O" or total[0][2]=="O" and total[1][2]=="O" and total[1][2]=="O" or total[0][0]=="O" and total[1][1]=="O" and total[2][2]=="O" or total[0][2]=="O" and total[1][1]=="O" and total[2][0]=="O":
            print("Gano O".upper())
            input("Presione Enter para salir")
            break
        empate=total[0].count("X") + total[0].count("O") + total[1].count("X") + total[1].count("O") + total[2].count("X") + total[2].count("O")
        if empate==9:
            print("Hubo un empate".upper())
            input("Presione Enter para salir")
            break
        print("\nAhora va O".upper())
        y=int(input("Seleccione del 1 al 3 para su casilla en orden vertical:"))
        x=int(input("Seleccione del 1 al 3 para su casilla en orden horizontal:"))
        if total[y-1][x-1]=="X":
            print("No puedes sobreescribir")
        else:
            total[y-1][x-1]="O"
            for i in total:
                print(i)
except Exception as error:
    print(f"Ups, parece que tuviste el error: {error}")
            
            
