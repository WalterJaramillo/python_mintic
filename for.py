"""
# FOR

for variable in elemento_iterable (lista, rango, etc.)
    BLOQUE DE INSTRUCCIONES
    
"""
contador = 0
resultado = 0

for contador in range(0,5):
    print("Voy por el "+ str(contador))

    resultado += contador

print(f"El resultado es: {resultado}")

# Ejemplo con tablas de multiplicar
print("\n################## EJEMPLO ###############################")

numero_usuario = int(input("¿De qué número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### TABLA DE MULTIPLICAR DEL NÚMERO {numero_usuario} ####")

for numero_tabla in range (1,11):

    if numero_usuario == 66:
        print("No se pueden mostrar números prohíbidos :(")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.")