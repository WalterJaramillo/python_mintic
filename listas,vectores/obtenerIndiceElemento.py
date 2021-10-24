'''
lista = [1, 50, 30]
if 50 in lista: # Imprime lo de abajo
    print("El número 50 existe en la lista")

otra_lista = ["perro", "gato", "conejo"]
if "caballo" in otra_lista: #No imprime nada
    print("caballo existe dentro de otra_lista")
    
lista = [1, 50, 30]
indice = lista.index(50)
print("El número 50 está en la posición {} de la lista".format(indice))

'''
listastring = ['hola','melo','cristian']
indice = listastring.index('hola')
print("El string hola está en la posición {} de la lista".format(indice))