print("Conversor de decimal a binario (8 bytes)")
binario=[]
numero_ingresado=int(input("Ingresar:"))
resto=0
for bina in range(8):
    resto=numero_ingresado%2
    binario.append(resto)
    numero_ingresado=numero_ingresado//2
binario.reverse()
print(binario)


