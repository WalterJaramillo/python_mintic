"""hallar el area del triangulo y el area de la circunferenica mediante funciones usando parametros y captura 

base * altura /2
pi * radio al cuadrado"""

"""area del triangulo"""
def area_tri (b, a):
    area=int (base) * int (altura) / 2.0
    print ("el resultado es: " + str (area))
    
print ("CALCULAR EL AREA DE UN TRIANGULO")
base=input("CUAL ES LA BASE: ")
altura=input("CUAL ES LA ALTURA: ")


area_tri(base,altura)

"""area de la circunferencia"""
def area_cir (b):
    pi= 3.14
    area= pi**2
    print ("el resultado es: " + str (area))
    
print ("CALCULAR EL AREA DEL LA CIRCUNFERENCIA")
radio=input("Indique el radio: ")


area_cir(radio)