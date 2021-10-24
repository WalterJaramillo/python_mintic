 nombre = input("digite su nombre: ")  #por defecto se guardara como cadena input guarda string
print(f"hola {nombre}")

nombre = int(input("digite su nombre: "))  #se debe transformar con int
print(f"hola {nombre}")

nombre = float(input("digite su nombre: "))  #se debe transformar con float
print(f"hola {nombre}")

nombre = bool(input("true or false "))  #se debe transformar con booleano
print(f"hola {nombre}")


cadena = input("ingrese su nombre: ")
print(cadena.center(50," ").upper())
print(cadena.center(50," ").lower())



import os
def get_name() -> str: 
    return input("Enter your name: ") 
if __name__ == '__main__': name=get_name() 
width = os.get_terminal_size().columns 
print(name.lower()) 
print(name.upper()) 
print(name.center(width))

linea = input("Indique un color")
print(linea.replace('Rojo', 'Blanco'))

lineao = input("Digite su nombre: ")
print(len(lineao))