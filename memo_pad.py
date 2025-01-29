import os
def create_directory(you):
    if os.path.exists(you)==False:
        os.mkdir(you)
        print("\nDirectorio creado exitosamente")
    else:
        print("\nYa hay un directorio existente")
def create_note(you, you2):
    if os.path.exists(you)==True:
        love=os.path.join(you, you2)
        if os.path.isfile(love)==False:
            si=open(love,"w")
            si.close()
            print("\nNota creada exitosamente")
        else:
            print(f"\nYa existe una nota con el nombre -{you2}-")
    else:
        print(f"\nNo existe un directorio con el nombre -{you}-")
def modify_note(you, you2):
    if os.path.exists(you)==True:
        love = os.path.join(you, you2)
        if os.path.isfile(love)==True:
            with open(love,"a") as f:
                f.write("\n")
                for i in range(20):
                    f.write("-")
                f.write("\n")
                f.write(input("Escribir aqui:"))
            print("\nNota modificada exitosamente")
        else:
            print(f"\nNo se ha encontrado la nota -{you2}- dentro del directorio -{you}-")
    else:
        print(f"\nNo se ha encontrado el directorio -{you}-")
def read_note(you, you2):
    if os.path.exists(you)==True:
        love = os.path.join(you, you2)
        if os.path.isfile(love)==True:
            with open(love,"r") as f:
                leer = f.read()
                print(leer)
        else:
            print(f"\nNo se ha encontrado la nota {you2} dentro del directorio {you}")
    else:
        print(f"\nNo se ha encontrado el directorio -{you}-")
def delete_directory(you):
    if os.path.exists(you) == True:
        if os.listdir(you)==None:
            os.rmdir(you)
            print(f"\nEl Directorio -{you}- ha sido borrado exitosamente")
        else:
            print(f"\nEl Directorio -{you}- debe estar vacio para poder borrarlo")
    else:
        print(f"\nNo hemos encontrado algun directorio con el nombre -{you}-")
def delete_note(you,you2):
    if os.path.exists(you) == True:
        love = os.path.join(you, you2)
        if os.path.isfile(love)==True:
            os.remove(love)
            print(f"\nLa Nota -{you2}-  dentro del directorio -{you}- ha sido borrada exitosamente")
        else:
            print(f"\nNo se ha encontrado la nota {you2} dentro del directorio {you}")
    else:
        print(f"\nNo se ha encontrado el directorio -{you}-")
def menu():
    print("-----Menu-----")
    print("Presione 1 para crear un directorio")
    print("Presione 2 para crear una nota dentro de un directorio")
    print("Presione 3 para modificar una nota dentro de un directorio")
    print("Presione 4 para leer una nota dentro de un directorio")
    print("Presione 5 para eliminar una nota")
    print("Presione 6 para eliminar un directorio")
    eleccion=int(input(":"))
    if eleccion==1:
        create_directory(you=input("\nColoque el nombre de su directorio:"))
    if eleccion==2:
        create_note(you=input("\nColoque el nombre de su directorio:"), you2=input("Coloque el nombre de su nota:"))
    if eleccion==3:
        modify_note(you=input("\nColoque el nombre de su directorio:"),you2=input("Coloque el nombre de su nota:"))
    if eleccion==4:
        read_note(you=input("\nColoque el nombre de su directorio:"), you2=input("Coloque el nombre de su nota:"))
    if eleccion==5:
        delete_note(you=input("\nColoque el nombre de su directorio:"), you2=input("Coloque el nombre de su nota:"))
    if eleccion==6:
        delete_directory(you=input("\nColoque el nombre de su directorio:"))
menu()


