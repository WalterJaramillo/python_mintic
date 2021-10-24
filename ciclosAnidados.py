cont = 1 
fin = int(input("Digite la cantidad de veces que desea realizar la operación: ")) 
while(cont <= fin): 
    for n in range(1,101,1): 
        print(n%2==0) 
        cont+=1