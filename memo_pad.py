import os
if os.path.exists("file_mom")==False:
    os.mkdir("file_mom")
def create_directory(you):
    love=os.path.join("file_mom",you)
    if os.path.exists(love)==False:
        os.mkdir(love)
        print("\nDirectorio creado exitosamente\n")
    else:
        print("\nYa hay un directorio existente\n")
def create_note(you, you2):
    love = os.path.join("file_mom", you)
    if os.path.exists(love)==True:
        love2=os.path.join(love, you2)
        if os.path.isfile(love2)==False:
            si=open(love2,"w")
            si.close()
            print("\nNota creada exitosamente\n")
        else:
            print(f"\nYa existe una nota con el nombre -{you2}-\n")
    else:
        print(f"\nNo existe un directorio con el nombre -{you}-\n")
def modify_note(you, you2):
    love = os.path.join("file_mom", you)
    if os.path.exists(love)==True:
        love2 = os.path.join(love, you2)
        if os.path.isfile(love2)==True:
            with open(love2,"a") as f:
                f.write("\n")
                for i in range(20):
                    f.write("-")
                f.write("\n")
                f.write(input("Escribir aqui:"))
            print("\nNota modificada exitosamente\n")
        else:
            print(f"\nNo se ha encontrado la nota -{you2}- dentro del directorio -{you}-\n")
    else:
        print(f"\nNo se ha encontrado el directorio -{you}-\n")
def read_note(you, you2):
    love = os.path.join("file_mom", you)
    if os.path.exists(love)==True:
        love2 = os.path.join(love, you2)
        if os.path.isfile(love2)==True:
            with open(love2,"r") as f:
                leer = f.read()
                print(leer)
        else:
            print(f"\nNo se ha encontrado la nota {you2} dentro del directorio {you}\n")
    else:
        print(f"\nNo se ha encontrado el directorio -{you}-\n")
    a = int(input("Presione 1 para volver al menu:"))
def delete_directory(you):
    love = os.path.join("file_mom", you)
    if os.path.exists(love) == True:
        if os.listdir(love)==[]:
            os.rmdir(love)
            print(f"\nEl Directorio -{you}- ha sido borrado exitosamente\n")
        else:
            print(f"\nEl Directorio -{you}- debe estar vacio para poder borrarlo\n")
    else:
        print(f"\nNo hemos encontrado algun directorio con el nombre -{you}-\n")
def delete_note(you,you2):
    love = os.path.join("file_mom", you)
    if os.path.exists(love) == True:
        love2 = os.path.join(you, you2)
        if os.path.isfile(love2)==True:
            os.remove(love2)
            print(f"\nLa Nota -{you2}-  dentro del directorio -{you}- ha sido borrada exitosamente\n")
        else:
            print(f"\nNo se ha encontrado la nota {you2} dentro del directorio {you}\n")
    else:
        print(f"\nNo se ha encontrado el directorio -{you}-\n")
def see_directorys():
    print("\nSus directorios vigentes son: \n")
    for i in os.listdir("file_mom"):
        print(i,"\n")
    a=int(input("Presione 1 para volver al menu:"))
def see_notes(you):
    print(f"\nSus notas vigentes dentro del directorio -{you}- son: \n")
    love = os.path.join("file_mom", you)
    for i in os.listdir(love):
        print(i,"\n")
    a = int(input("Presione 1 para volver al menu:"))
def menu():

    while 0!=1:
        print("-----Menu-----")
        print("\nPresione 0 para salir")
        print("\nPresione 1 para crear un directorio")
        print("\nPresione 2 para crear una nota dentro de un directorio")
        print("\nPresione 3 para modificar una nota dentro de un directorio")
        print("\nPresione 4 para ver sus directorios existentes")
        print("\nPresione 5 para ver sus notas dentro de un directorio")
        print("\nPresione 6 para leer una nota dentro de un directorio")
        print("\nPresione 7 para eliminar una nota")
        print("\nPresione 8 para eliminar un directorio")
        eleccion=int(input(":"))
        if eleccion==0:
            break
        if eleccion==1:
            create_directory(you=input("\nColoque el nombre de su directorio:"))
        if eleccion==2:
            create_note(you=input("\nColoque el nombre de su directorio:"), you2=input("Coloque el nombre de su nota:"))
        if eleccion==3:
            modify_note(you=input("\nColoque el nombre de su directorio:"),you2=input("Coloque el nombre de su nota:"))
        if eleccion==4:
            see_directorys()
        if eleccion==5:
            see_notes(you=input("\nColoque el nombre de su directorio:"))
        if eleccion==6:
            read_note(you=input("\nColoque el nombre de su directorio:"), you2=input("Coloque el nombre de su nota:"))
        if eleccion==7:
            delete_note(you=input("\nColoque el nombre de su directorio:"), you2=input("Coloque el nombre de su nota:"))
        if eleccion==8:
            delete_directory(you=input("\nColoque el nombre de su directorio:"))
menu()
