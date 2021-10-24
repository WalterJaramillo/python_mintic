lista = [1,2,4,5]
lista.append(6)

lista.pop()#elimina el ultimo
lista.pop(2) #pasarle el indice
lista.remove(5) #elimina direcatamente lo que esta en la listas
lista.clear()#borra todo
lista.reverse()
lista.insert(2,3) #insertar
lista.extend([7,8,9]) #extender
lista = [1,2,4,5]*2
lista.sort()#ordenar accedente
lista.sort(reverse=True) #Ordena desendente

print(lista.index(5))#buscar
print(lista.count(1))#contar
print(7 in lista)
print(lista)
print(len(lista))

lis = [2, 1, 3, 5, 4, 3, 8]