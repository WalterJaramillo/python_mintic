"""Saber la fecha funcion streftime"""
import datetime 
def fecha(): 
    ahora = datetime.datetime.now()
    print(ahora.strftime('%d/%m/%Y %H: %M: %S')) 
fecha()
fecha()
"""seno"""
import math
def xsen(x):
    return x*math.sin(x)
print(xsen(math.pi/2))
"""edad con funcion"""
def esmayor(edad):
    if edad < 18:
        resultado = False
    else:   
        resultado =True
    return resultado
print(esmayor(19))

"""suma con mas de 2 params"""
def suma(a,b,c):
    suma = a+b+c
    print(sum)
suma(8,9,3)

"""suma con mas de 2 params"""
def suma(a,b,c):
    suma = a+b+c
    print(sum)
suma(8,9,3)

"""other example"""
def resta(a,b):
    r = a-b
    print(r)
n = 0
while(n<3): 
    a=int(input("a: "))
    b=int(input("b: "))
    n+=1
resta(8,9)
###########################################
a = int(input("Indique un numero"))
if a < 0:
    print("oye por favor mete un numero mayor a cero")
print(f"tu pusiste el numero {a}")
#######################################################
edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")