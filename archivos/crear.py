'''
from io import open
file = open('file.txt', 'w')
frase = "estamos\nmelos"
file.write(frase)
file.close()

file = open('file.txt', 'r')
texto = file.read() # lee todo el texto todas las lineas y almacena en una variable
file.close()
print(texto)
'''
file = open('file.txt', 'r')
lineas_texto = file.readlines() # guarda las lineas del texto en una list y es manipulable
file.close()
print(lineas_texto) # imprime todo el texto en lista
print(lineas_texto[0])
print(lineas_texto[1])
print(len(lineas_texto))


file = open('file.txt', 'a')
file.write("\n es una buena oportunidad para aprender") #Esta linea no sera en la segunda linea si no en la tercera para eso el \n
file.close()



file = open('file.txt', 'a')
file.write(" es una buena oportunidad para aprender") #Esta linea no sera en la segunda linea si no en la tercera para eso el \n
file.close()



print(file.read())  #esto no leera 2 veces la misma información por el append lo dejara el puntero al final de todas las lineas
print(file.read())

print(file.read())  
file.seek(0)            #lea el archivo y envie el cursor a la posicioón 0 y lee esto saldra 2 veces en el print
print(file.read())

#seek(#numero de caracter donde queremos que se posiciones el cursor)



