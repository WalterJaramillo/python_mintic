import pathlib
import os

ver_listado =1
ver_listado_filtrado =2
agregar_beneficiario =3
buscar_beneficiario =4
borrar_beneficiario =5
salir =6

def mostrar_menu():
    print(f'''                         Menu Principal     
{ver_listado} Ver listado
{ver_listado_filtrado} Ver Listado filtrado
{agregar_beneficiario} Agregar beneficiario
{buscar_beneficiario} Buscar beneficiario
{borrar_beneficiario} Borrar beneficiario
{salir} salir''')

def cargar_agenda(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo, 'r').exists():
        with open(nombre_archivo) as archivo:
            for linea in archivo:
                nombres,id,telefono = linea.strip().splitlines()
                agenda.setdefault(id, (nombres,telefono))
    else:
        with open(nombre_archivo, 'w') as archivo:
            pass


def agregar_contacto(agenda, nombre_archivo):

    print('                    Digite la información del beneficiario a agregar:')
    nombres = input("indica tu nombre: ")
    cedula = input('indica tu cedula: ')
    if agenda.get(cedula):
        print('El beneficiario ya existe vuelve a intentar')
    else:
        telefono = input('telefono: ')
        agenda.setdefault(cedula, (nombres,telefono))
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f'{nombres}\n{cedula}\n{telefono}\n')
        print('El beneficiario ha sido agregado al listado')
def mostrar_contactos(agenda):

    print('Listado de beneficiarios:')
    if len(agenda) > 0:
        for id, datos in agenda.items():
            print(f'nombres: {datos[0]}')
            print(f'cedula: {id}')
            print(f'telefono: {datos[1]}')
            print('*'*50)
    else:
        print('No hay conctactos registrados')

def buscar_contacto(agenda):
    if len(agenda) > 0:
        nombre = input('Digite el nombre y apellido del beneficiario a buscar: ')
        for id, datos in agenda.items():
            if nombre in datos[0]:
                print(f'Nombre: {datos[0]}')
                print(f'cedula: {id}')
                print(f'telefono: {datos[1]}')
                print('*'*50)
    else:
        print('No se encuentra el beneficiario en la agenda')

def buscar_contacto_filtrado(agenda):
    if len(agenda) > 0:
        nombre = input('Digite la letra por la que empiezan los beneficiarios: ')
        print("Listado filtrado de beneficiarios: ")
        for id, datos in agenda.items():
            if nombre in datos[0]:
                print(f'Nombre: {datos[0]}')
                print(f'cedula: {id}')
                print(f'telefono: {datos[1]}')
                print('*'*50)
    else:
        print('No se encuentra el beneficiario en la agenda')


def borrar_contacto(agenda):
    if len(agenda) > 0:
        cedula = input('Digite la cedula del beneficiario a borrar:')
        with open('agenda.txt', 'r') as f:
            lineas = f.read().splitlines()
            indice = lineas.index(cedula)
            del lineas[indice-1:indice+2]
        with open('agenda.txt', 'w') as f:
            for linea in lineas:
                f.write(linea+"--")


        print("El beneficiario ha sido borrado")

    else:
        print('No se encuentra la cedula del beneficiario registrada')



def main():
    continuar = True
    agenda = dict()
    nombre_archivo = 'agenda.txt'
    cargar_agenda(agenda, nombre_archivo)
    while continuar:
        mostrar_menu()
        opc = int(input("Selecciona una opción: "))

        if opc ==  ver_listado:
            mostrar_contactos(agenda)
        elif opc == ver_listado_filtrado:
            buscar_contacto_filtrado(agenda)
        elif opc ==  agregar_beneficiario:
            agregar_contacto(agenda,nombre_archivo)
        elif opc ==  buscar_beneficiario:
            buscar_contacto(agenda)
        elif opc ==  borrar_beneficiario:
            borrar_contacto(agenda)
        elif opc == salir:
            continuar = False
        else:
            print("Opción no valida")
    print("Hasta pronto")
if __name__=='__main__':
    main()