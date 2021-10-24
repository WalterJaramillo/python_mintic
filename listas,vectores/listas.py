'''
lista = [1,2,3,4,5,6,7,8,9]
    
lista.append(10)
print(lista)
'''

'''
numbers = list(range(10))  #range -1 return only a paremeter
print(numbers)

numbers = list(range(3,8)) # two parameters
print(numbers)

numbers = list(range(5,20,2)) #three parameters
print(numbers)

for i in range(5):
    print("hello!")
    
for i in range(0, 20,2):
    print(i)
    
'''
#corte de listas
'''
squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1]) # siempre llegara uno menos del numero indicado

squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[:7])
print(squares[7:])

squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[::2])
print(squares[2:8:3])

squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[1:-1])  # siempre llegara uno menos del numero indicado aun en negativo

'''
pelis = ["uno", "dos", "tres"]
for i in pelis:
    print(f"{pelis.index(i)+1}. {i}")
    