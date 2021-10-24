list = range(1,11)
for x in list:
    if x == 9:
        break  # todo el bucle termina o rompe todo el ciclo, no ejecuta nada de lo de abajo
    if x == 5:
        continue # se salta el el ciclo cuando se cumpla dicha condición, no hara lo de abajo
    print(f"Número: {x}")