eleccion=int(input("Ingrese la cantidad de matrices que desea sumar:"))
columna=int(input("Coloque la cantidad de columnas para su matriz:"))
fila=int(input("Coloque la cantidad de filas para su matriz:"))
matriz_mix=[]
for i in range(eleccion):
    print("Vamos con la matriz num:",i+1)
    matrix=[]
    for colum in range (columna):
        lista=[]
        for fil in range (fila):
            num=int(input(f"Ingrese su numero para la columna {colum+1} en la fila {fil+1} :"))
            lista.append(num)
        matrix.append(lista)
    matriz_mix.append(matrix)
matrix_sumada=[]
for desarme in range(columna):
    matrix=[]
    for desarme_2 in range(fila):
        suma=0
        for desarme_3 in matriz_mix:
            suma+=desarme_3[desarme][desarme_2]
        matrix.append(suma)
    matrix_sumada.append(matrix)
matriz_mix.append(matrix_sumada)
for desarme in range(columna):
    for posicion in range(len(matriz_mix)):
        if columna==1:
            if posicion==eleccion-1:
                print(matriz_mix[posicion][desarme], end=" = ")
            if posicion<eleccion-1:
                    print(matriz_mix[posicion][desarme], end=" + ")
            if posicion>eleccion-1:
                    print(matriz_mix[posicion][desarme],end="   ")
        else:
            if desarme!=1:
                print(matriz_mix[posicion][desarme], end="   ")
            else:
                if desarme==1 and posicion==eleccion-1:
                    print(matriz_mix[posicion][desarme], end=" = ")
                if desarme==1 and posicion<eleccion-1:
                    print(matriz_mix[posicion][desarme], end=" + ")
                if desarme==1 and posicion>eleccion-1:
                    print(matriz_mix[posicion][desarme],end="   ")
a=input("Enter:")
    print()
        
    
        
            

        
        
       
     
        
    
    
            

        
