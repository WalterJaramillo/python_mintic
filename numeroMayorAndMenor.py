max = 0
for x in range(1,6,1):
    cap = int(input("Indique un número: "))
    if cap > max:
        max = cap
    #cap = int(input("Indique un número: ")) # debe estar debajo de if ya que si no se cumple el condicion 
                                            #lee esta linea, pero la ultima captura no funciona, la solucion ya esta
                                            #el rago es si quiero 5 numeros: 2,3,4,5,6
print(f"el numero mayor es: {max} ")