n = int(input("Indique el numero de la cantidad de notas a promediar: "))
i = 1
suma = 0

while i<=n:
    nota = float(input("Indique su primer nota: "))
    suma += nota
    i += 1
prom = suma/n
print(f"el promedio de las notas es {prom}")
    