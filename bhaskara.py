while 0<1:
    grado_dos=int(input("Coloque el valor de X**2:"))
    grado_uno=int(input("Coloque el valor de X:"))
    independiente=int(input("Coloque el valor del numero independiente:"))
    confirm=input(f"¿Su ecuacion es esta?: {grado_dos}X**2 {grado_uno}X {independiente}\n")
    if confirm.lower()=="si":
        break
proceso=(grado_uno)**2-4*grado_dos*independiente
if proceso<=0:
    print("Su ecuacion no tiene solucion dentro de los numeros reales")
proceso=proceso**(1/2)
resultado_1=(-grado_uno+proceso)/(2*grado_dos)
resultado_2=(-grado_uno-proceso)/(2*grado_dos)
print(f"Los resultados de su ecuacion son: {resultado_1} y {resultado_2}")
