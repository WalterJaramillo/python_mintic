#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------
cont_total_dias = 0 
cont_dias_min_error = 0
cont_dias_max_error = 0
cont_dias_sin_error = 0
cont_total_dias_error = 0
temp_prom_min = 0
temp_prom_max = 0
temp_max =1
temp_min =1
suma_promedio_minimo= 0
suma_promedio_maximo= 0

while temp_min != 0 and temp_max !=0:
    temp_min = float(input('indique el valor minimo de temperatura: '))
    temp_max = float(input('indique el valor maximo de temperatura: '))
    if temp_min < 5 or temp_max > 35:
        if temp_min == 0 and temp_max ==0:
            break
        if temp_min < 5:
            cont_dias_min_error += 1
            #suma_promedio_minimo += temp_min  
            print("<--------Nuevo dia ------------>")
            #print(f"los dias con error minimos fueron: {cont_dias_min_error}")
            continue #pasa de nuevo al ciclo
        elif temp_max > 35:
            cont_dias_max_error += 1
            #suma_promedio_maximo += temp_max
            print("<--------Nuevo dia ------------>")
            #print(f"los dias con error maximos fueron: {cont_dias_max_error}")
            continue #pasa de nuevo al ciclo
    if temp_min > 5 and temp_max <35:
        cont_dias_sin_error += 1
        if temp_min > 5:
            suma_promedio_minimo += temp_min 
            if temp_max < 35:
                suma_promedio_maximo += temp_max
        print("<--------Nuevo dia ------------>")
        continue
    
    
cont_total_dias_error = cont_dias_min_error + cont_dias_max_error
cont_total_dias = cont_dias_min_error + cont_dias_max_error + cont_dias_sin_error 
temp_prom_min = suma_promedio_minimo/ cont_dias_sin_error if suma_promedio_minimo != 0 else 0
temp_prom_max = suma_promedio_maximo/ cont_dias_sin_error if suma_promedio_maximo != 0 else 0

print(f"Dias totales : {cont_total_dias}")
print(f"Dias totales con error son: {cont_total_dias_error}")
print(f"Dias con temperaturas menores a 5 grados: {cont_dias_min_error}")
print(f"Dias con temperaturas mayores a 35 grados: {cont_dias_max_error}")
print(f"Temperatura media minima es: {temp_prom_min}")
print(f"Temperatura media maxima es: {temp_prom_max}")


