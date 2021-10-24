import numpy as np 
numero_filas=int(input("Digite número de filas:")) 
numero_columnas=int(input("Digite número de columnas:")) 
mat1 =np.zeros((numero_filas,numero_columnas)) 
i=0 
while(i<numero_filas): 
    j=0 
    while(j<numero_columnas): 
        mat1[i][j]= int(input("Digite valor:")) 
        j=j+1 
    i=i+1 
print(mat1)
