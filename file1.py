abrir = open('archivo1406.txt') 
print(abrir)


abrirlinea = open('archivo1406.txt') 
contador = 0 
for linea in abrirlinea: 
    contador = contador + 1 
print('Contador de líneas:', contador)


abrirlinea = open('archivo1406.txt') 
contador = 0 
for linea in abrirlinea: 
    contador += 1 
    print('Contador de líneas:', contador)
    
manejador_archivo = open('archivo1406.txt') 
inp = manejador_archivo.read() 
print(len(inp))



man_a = open('archivo1406.txt') 
contador = 0 
for linea in man_a: 
    if linea.startswith('h'): 
        print(linea)