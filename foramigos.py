

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