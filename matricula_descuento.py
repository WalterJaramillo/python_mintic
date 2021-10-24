#Presentado a Fabian Junco
#Por Walter Jaramillo Cubillos GRUPO 6
# CC  1074159366
nombres = ''                                    #Variable que contiene nombres y apellidos
edad = 0                                        #Variable que contiene la edad
ingreso_familiar = 0                            #Variable que contiene el ingreso familiar
total_porcentaje = 0                            #Variable que contiene el porcentaje total de descuento en la matricula                               #
salario_minimo = 900.000                        #Salario minimo 'inventado es modificable y no afecta el programa'

print(nombres:=(input('Indique sus nombres y apellidos \n')))                            #lectura de los nombres
print(edad:=int(input('Indique su edad \n ')))                                           #lectura de edad
print(ingreso_familiar:=float(input('Indique su ingreso familiar \n ')))                 #lectura de ingreso familiar
print(puntaje_examen:=int(input('Indique su puntaje de examen de 0 a 100 \n ')))         #lectura de puntaje examen

if edad >= 15 and edad <= 18:                                                            #validaciones con edad mayor o igual a 15 y menor o igual a 18
    total_porcentaje = total_porcentaje + 0.25
    if ingreso_familiar <= salario_minimo and puntaje_examen >= 80 and puntaje_examen < 86:
        total_porcentaje = total_porcentaje + 0.30 + 0.30
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 30%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.30 +0.35
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 30%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.30 +0.40
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 30%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.30 +0.45
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 30%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 20%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 20%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 20%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 20%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 10%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 10%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 10%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 10%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 10%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 5%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 5%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 5%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 5%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 5%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 0%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 0%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 0%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 0%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 25%, Desc.ing.familiar: 0%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')
elif edad >= 19 and edad <= 21:                              #validaciones con edad mayor o igual a 19 y menor o igual a 21
    total_porcentaje = total_porcentaje + 0.15
    if ingreso_familiar <= salario_minimo and puntaje_examen >= 80 and puntaje_examen < 86:
        total_porcentaje = total_porcentaje + 0.30 + 0.30
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 30%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.30 +0.35
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 30%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.30 +0.40
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 30%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.30 + 0.45
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 30%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 20%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 20%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 20%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 20%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 10%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 10%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 10%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 10%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 10%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 5%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 5%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 5%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 5%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 5%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 0%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 0%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 0%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 0%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 15%, Desc.ing.familiar: 0%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')
elif edad >= 22 and edad <= 25:                                  #validaciones con edad mayor o igual a 22 y menor o igual a 25
    total_porcentaje = total_porcentaje + 0.10
    if ingreso_familiar <= salario_minimo and puntaje_examen >= 80 and puntaje_examen < 86:
        total_porcentaje = total_porcentaje + 0.30 + 0.30
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 30%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.30 +0.35
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 30%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.30 +0.40
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 30%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.30 +0.45
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 30%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 20%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 20%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 20%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 20%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 10%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 10%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 10%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 10%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 10%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 5%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 5%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 5%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 5%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 5%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 0%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 0%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 0%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 0%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 10%, Desc.ing.familiar: 0%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

elif edad >= 25:                                 #validaciones con edad mayor o igual a 25
    total_porcentaje = total_porcentaje + 0
    if ingreso_familiar <= salario_minimo and puntaje_examen >= 80 and puntaje_examen < 86:
        total_porcentaje = total_porcentaje + 0.30 + 0.30
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 30%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.30 +0.35
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 30%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.30 +0.40
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 30%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.30 +0.45
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 30%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar <= salario_minimo and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 20%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 20%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 20%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.20
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 20%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2 and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 30%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 10%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 10%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 10%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.10
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 10%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 10%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 5%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 5%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 5%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4 and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45 + 0.5
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 5%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 5%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')

    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 80 and puntaje_examen < 86 :
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 0%, Desc. examen: 30%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 86 and puntaje_examen < 91:
        total_porcentaje = total_porcentaje + 0.35
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 0%, Desc. examen: 35%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 91 and puntaje_examen < 96:
        total_porcentaje = total_porcentaje + 0.40
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 0%, Desc. examen: 40%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen >= 96:
        total_porcentaje = total_porcentaje + 0.45
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 0%, Desc. examen: 45%, Total: ', int(total_porcentaje * 100),'%')
    elif ingreso_familiar > salario_minimo*4  and puntaje_examen < 80:
        total_porcentaje = total_porcentaje + 0.30
        print('nombre: ',nombres, 'Desc. edad: 0%, Desc.ing.familiar: 0%, Desc. examen: 0%, Total: ', int(total_porcentaje * 100),'%')
