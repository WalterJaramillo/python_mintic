'''sacar la raiz cuadrade un numero siempre debe ser positivo'''
import math

a = int(input("digite un numero: "))

while a < 0:
    print('Su numero es negativo, vuelve a intentar: ')
    a = int(input("digite un numero: "))

print(f"\n Su raiz cuadrada es: {(math.sqrt(a)):.2f}")