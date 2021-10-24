while True:
    edad = int(input("indique edad: "))
    if edad >= 18:
        print("es mayor de edad")
        continue #pasa de nuevo al ciclo
    print('xxxxxx')
    if edad > 0 and edad <=7:
        print('estas en el ciclo vital de la infancia')
    break
print("proceso terminado")