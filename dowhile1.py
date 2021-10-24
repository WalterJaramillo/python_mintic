"""
x = 25
while True: 
    print(x) 
    x+=1 
    if(x>=10): 
        break 
print("fin del ciclo")
"""

while True: 
    print(" 1. ciclo de 1 a 10 2. resta 3 multiplicación, 4 salir") 
    op = int(input("Digite su opción")) 
    i=5 
    while(i>=1): 
        print(i) 
        i-=1
    if op == 1: 
        i=0 
        while(i<=10): 
            print(i) 
            i=i+1
    if op == 2: 
        print("hace el proceso de resta") 
    if op == 3: 
        print("hace el proceso de multiplicación") 
    if op == 4: 
        break 
print("fin del menu")