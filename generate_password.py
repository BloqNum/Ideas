import random
import string
print("\n¡AVISO PARA LOS ABUELOS!\nSi estas leyendo esto, te aviso que cuando pongas un valor en donde se te indica, luego de colocarlo presiones enter\n")
def generador_contraseña(eleccion):
    """
    Funcion para generar contraseñas aleatorias con caracteres de letras en minusculas y mayusculas, ademas de numeros
    :param eleccion: Es el valor el cual indicara cuantos caracteres tendra tu contraseña generada aleatoriamente
    :return: Devuelve una lista con los caracteres de tu contraseña
    """
    contraseña = []
    ran = 0
    for i in range(eleccion):
        ran=random.randint(1,3)
        if ran==1:
            contraseña.append(random.choice(string.ascii_lowercase))
        if ran==2:
            contraseña.append(random.choice(string.ascii_uppercase))
        if ran==3:
            contraseña.append(random.choice(string.digits))
    return contraseña
try:
    cantidad=int(input("Coloque la cantidad de caracteres que tendra su contraseña (minimo 12): "))
    while 0!=1:
        contraseña_final="".join(generador_contraseña(eleccion=cantidad))
        print(f"\nSu contraseña generada aleatoriamente es: {contraseña_final}\nPuede copiarla")
        finalizacion=int(input("\nSi esta satisfecho con su contraseña presione 1, sino, presione 2:"))
        if finalizacion==1:
            print("\nGracias por elegirnos")
            break
    input("\nPresione enter para salir:")
except Exception as mistake:
    print(f"Ups, parece que hubo un error en la ejecucion del programa\nEse error es: {mistake}")