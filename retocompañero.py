from math import pi
def circunferencia(r): 
    circunferencia = pi * (r**2) 
    return circunferencia 
r = float(input("Ingrese el radio: ")) 
resultado = circunferencia(r) 
print('La circunferencia es: {:.2f}'.format(resultado))