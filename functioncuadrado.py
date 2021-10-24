#funcion con parametro
def cuadrado(x):
    return x**2

print(cuadrado(2))

#funcion sin parametro
def imprimir():
    print("Walter")
    
imprimir() 
 

"""se llama por fuera"""


def suma(algoa,algob):
    print(algoa+algob)
    return(algoa+algob)
    
a = int(input("digite el primer valor \n"))
b = int(input("digite el segundo valor \n"))
suma(a,b)
print(suma(a,b))


def resta(algoc,algod):
    print(f"el valor de la resta es {algoc-algod}")
c = int(input("digite el primer valor \n"))
d = int(input("digite el segundo valor \n"))
resta(c,d)

