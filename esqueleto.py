# Les comparto la información del código trabajado en el último encuentro
def borrar():
    posborrar= int(input("Digite posición a borrar: "))
    with open("automotor.txt", "r") as f:
        list = f.read().splitlines()
        indice = list.index(list[posborrar])
        del list[indice-1:indice+2]
    with open("automotor.txt", "w") as f:
        for line in list:
             f.write(line+"\n")
def imprimir():
    archivo = open('automotor.txt','r')
    contenido= archivo.read()
    print(contenido)
    archivo.close()
def escribirr():
    archivo = open("automotor.txt","a")
    placa=input("Digite la placa: ")
    archivo.write(placa+" ")
    color=input("Digite el color")
    archivo.write(color+"\n")
    archivo.close()
def buscar():
    archivo = open('automotor.txt','r')
    contenido= archivo.read()
    palabra = contenido.split()
    print(palabra)
    i=0
    e=0
    buscarp = input("digite la palabra a buscar:")
    while i<len(palabra):
        if palabra[i] == buscarp:
            e=e+1
            print(palabra[i]+"")
            print(palabra[i+1])
            break
            i+=1
    if e>=1:
        print("la palabra",buscarp, "fue encontrada")
    letra=palabra[i] # palabra
    print("la primera letra es: ", letra[0])
    #primera letra
    archivo.close()
while True:
    print("1. Registrar automotor")
    print("2. Buscar registro y primera letra")
    print("3. Imprimir registros")
    print("4. Borrar")
    print("5. Salir")
    op=int(input("Digite su opción----> "))
    if op==1:
        escribirr()
    if op==2:
        buscar()
    if op==3:
        imprimir()
    if op==5:
        print("Vuelve pronto a tu compraventa bye")
    break
    if op==4:
        borrar()