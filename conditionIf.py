'''
hacer un programa que me diga si el numero ingresado es positivo o es negativo
'''
a = int(input('numero --> '))

if a > 0:
    print("numero es mayor a cero")
elif a == 0:
    print("numero es igual a cero")
else:
    print("numero es menor a cero")
print(a)