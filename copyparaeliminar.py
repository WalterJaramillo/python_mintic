nombres = input("indique nombres: ")             
edad = int(input("indique edad: "))      
puntaje_examen = int(input("Indique puntaje: "))                                    
ingreso_familiar = float(input("indique ingreso familiar: "))           

porcentaje_edad = 0
porcentaje_ingreso_familiar = 0
porcentaje_puntaje_ingreso = 0
salario_minimo = 908.526
ingreso_familiar *= salario_minimo 

if edad >= 15 and edad <= 18: 
    porcentaje_edad = 25
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 30
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 35
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 40
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 20
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 10
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 5
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(porcentaje_edad)
            print(porcentaje_puntaje_ingreso)
            print(porcentaje_ingreso_familiar)
            print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*4:
        porcentaje_ingreso_familiar = 0
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45 
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
        
elif edad >= 19 and edad <= 21:
    porcentaje_edad = 15
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 30
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 35
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 40
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 20
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 10
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 5
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*4:
        porcentaje_ingreso_familiar = 0
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
        
elif edad >= 22 and edad <= 25: 
    porcentaje_edad = 10
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 30
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 35
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso =40
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 20
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 10
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 5
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*4:
        print("soy el salario")
        porcentaje_ingreso_familiar = 0
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
elif edad >= 25: 
    porcentaje_edad = 0
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 30
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 35
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 40
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 20
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 10
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 5
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
        total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)
    elif ingreso_familiar > salario_minimo*4:
        porcentaje_ingreso_familiar = 0
        if ingreso_familiar <= salario_minimo:
            porcentaje_ingreso_familiar = 30
            if puntaje_examen >= 80 and puntaje_examen < 86:
                porcentaje_puntaje_ingreso = 30
            elif puntaje_examen >=86 and puntaje_examen < 91:
                porcentaje_puntaje_ingreso = 35
            elif puntaje_examen >= 91 and puntaje_examen < 96:
                porcentaje_puntaje_ingreso = 40
            elif puntaje_examen >= 96:
                porcentaje_puntaje_ingreso = 45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
        print(porcentaje_edad)
        print(porcentaje_puntaje_ingreso)
        print(porcentaje_ingreso_familiar)
        print(total_porcentaje)