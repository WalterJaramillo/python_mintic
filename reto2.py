
nombres = input("indique nombres: ")             
edad = int(input("indique edad: "))                                          
ingreso_familiar = float(input("indique ingreso familiar: "))           
puntaje_examen = int(input("Indique puntaje: "))

salario_minimo = 1.0
porcentaje_edad = 0
porcentaje_ingreso_familiar = 0
porcentaje_puntaje_ingreso = 0
total_porcentaje = 0


if edad >= 15 and edad <= 18: 
    porcentaje_edad = 0.25
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 0.20
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 0.10
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 0.5
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*4:
        porcentaje_ingreso_familiar = 0
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45 
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        
elif edad >= 19 and edad <= 21:
    porcentaje_edad = 0.15
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 0.20
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 0.10
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 0.5
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*4:
        porcentaje_ingreso_familiar = 0
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
elif edad >= 22 and edad <= 25: 
    porcentaje_edad = 0.10
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 0.20
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 0.10
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 0.5
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*4:
        porcentaje_ingreso_familiar = 0
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
elif edad >= 25: 
    porcentaje_edad = 0
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo and ingreso_familiar <= salario_minimo*2:
        porcentaje_ingreso_familiar = 0.20
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*2 and ingreso_familiar <= salario_minimo*3:
        porcentaje_ingreso_familiar = 0.10
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*3 and ingreso_familiar <= salario_minimo*4:
        porcentaje_ingreso_familiar = 0.5
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
            
    elif ingreso_familiar > salario_minimo*4:
        porcentaje_ingreso_familiar = 0
    if ingreso_familiar <= salario_minimo:
        porcentaje_ingreso_familiar = 0.30
        if puntaje_examen >= 80 and puntaje_examen < 86:
            porcentaje_puntaje_ingreso = 0.30
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >=86 and puntaje_examen < 91:
            porcentaje_puntaje_ingreso = 0.35
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 91 and puntaje_examen < 96:
            porcentaje_puntaje_ingreso = 0.40
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
        elif puntaje_examen >= 96:
            porcentaje_puntaje_ingreso = 0.45
            total_porcentaje = porcentaje_edad + porcentaje_ingreso_familiar + porcentaje_puntaje_ingreso
            print(f"{porcentaje_edad:,.2f}, {porcentaje_ingreso_familiar:,.2f},{porcentaje_puntaje_ingreso:,.2f} , {total_porcentaje:,.2f}")
