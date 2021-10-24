#----------------------------------------------------
#		Grupo # 6
#       Presentado a : Ralando Junco
#       Estudiante: Walter Jaramillo
#       cc: 1074159366
#----------------------------------------------------

cont_total_dias = 0 
cont_dias_min_error = 0
cont_dias_max_error = 0
cont_dias_sin_error = 0
cont_total_dias_error = 0
cont_ambos_error = 0
temp_prom_min = 0
temp_prom_max = 0
temp_max =1
temp_min =1
suma_promedio_minimo= 0
suma_promedio_maximo= 0
porecentaje_dias_error= 0


# Ciclo while: linea 22 a linea 44
while temp_min != 0 and temp_max !=0:
    temp_max = float(input('indique el valor maximo de temperatura: '))
    temp_min = float(input('indique el valor minimo de temperatura: '))
    if temp_min < 5 or temp_max > 35:
        if temp_min == 0 and temp_max ==0:
            break
        elif temp_max > 35 and temp_min <5:
            cont_ambos_error += 1
            print("<--------Nuevo dia ------------>")
            continue
        elif temp_max > 35:
            cont_dias_max_error += 1
            print("<--------Nuevo dia ------------>")
            continue 
        elif temp_min < 5:
             cont_dias_min_error += 1
             print("<--------Nuevo dia ------------>")
             continue 
    if temp_min > 5 and temp_max <35:
        cont_dias_sin_error += 1
        if temp_min > 5:
            suma_promedio_minimo += temp_min 
        if temp_max < 35:
            suma_promedio_maximo += temp_max
        print("<--------Nuevo dia ------------>")
        continue
    elif temp_max == 35 and temp_min == 5:
         cont_dias_sin_error += 1
         suma_promedio_maximo += temp_max
         suma_promedio_minimo += temp_min
         continue
    elif temp_max == 35 and temp_min > 5:
         cont_dias_sin_error += 1
         suma_promedio_maximo += temp_max
         suma_promedio_minimo += temp_min
         continue
print("<------------------Resultado------------------>")
    
#Procesos: linea 47 a linea 51
cont_total_dias_error = cont_dias_min_error + cont_dias_max_error + cont_ambos_error
cont_total_dias = cont_dias_min_error + cont_dias_max_error + cont_dias_sin_error + cont_ambos_error
ambos_error = cont_ambos_error 
temp_prom_min = suma_promedio_minimo/ cont_dias_sin_error if suma_promedio_minimo != 0 else 0
temp_prom_max = suma_promedio_maximo/ cont_dias_sin_error if suma_promedio_maximo != 0 else 0
porecentaje_dias_error = (cont_total_dias_error * 100) / cont_total_dias if cont_total_dias_error !=0 else 0

# Salidas: Linea 54 a linea 60
print(f"Dias totales en campo : {cont_total_dias}")
print(f"Dias totales con error son: {cont_total_dias_error}")
print(f"Dias con temperaturas menores a 5 grados: {cont_dias_min_error}")
print(f"Dias con temperaturas mayores a 35 grados: {cont_dias_max_error}")
print(f"Dias con ambas temperaturas en error {ambos_error}")
print(f"Temperatura media maxima sin tener encuenta dias con error: {temp_prom_max}")
print(f"Temperatura media minima sin tener encuenta dias con error: {temp_prom_min}")
print(f"El porcentaje de dias con error es : {porecentaje_dias_error}")

    




