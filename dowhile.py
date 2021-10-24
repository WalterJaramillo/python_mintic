x= 1 
while x<10: 
    print(x) 
    x=x+1 
print("fin del while")
    
x=777 
while True: 
    print(x) 
    x=x+1 
    if x>=10: 
        break 
print("fin del ciclo")


while True: 
    print("1 sumar, 2 restar y 3 para salir") 
    x = int(input("ingrese su opción")) 
    if x == 1: 
        n = 1
        while n<5:
            print(n)
            n+=1
        print("hace la suma") 
        if x == 2: 
            print("hace la resta") 
        if x==3: 
            break 
print("saliste del menu")



while True: 
    print("1 imprimir numeros del 1 al 5, 2 restar y 3 para salir")
    x = int(input("ingrese su opción")) 
    if x == 1: 
        n = 1 
        while(n<=5): 
            print(n) 
            n+=1 
    if x == 2: 
        n = 10 
        while(n>=5): 
            print(n)
            n-=1 
    if x==3: 
        break 
print("saliste del menu")