name = input("Indique el nombre: ")
ht = int(input("Horas Trabajadas: "))
vh = float(input("Valor Hora: "))

def sueldoBruto_print(ht,vh):
    if ht > 40:
        vhe = (ht - 40) * 1.5*vh
        htn_print = 40 * 10000
        htn = 40
        sb = (htn*vh) + vhe
        print(f"Horas Trabajadas Normales {htn_print}")
        print(f"Horas Extra {vhe}")
        print(f"Salario Bruto {sb}")
        return sb
    elif ht <= 40:
        vhe = 0
        htn = ht*vh
        sb = htn
        print(f"Horas Trabajadas Normales {htn}")
        print(f"Horas Extra {vhe}")
        print(f"Salario Bruto {sb}")
        
def sueldoBruto_return(ht,vh):
    if ht > 40:
        vhe = (ht - 40) * 1.5*vh
        htn = 40
        sb = (htn*vh) + vhe
        return sb
    elif ht <= 40:
        vhe = 0
        htn = ht*vh
        sb = htn
        return sb
sb=(sueldoBruto_return(ht,vh)) #esta var retorna el sueldo bruto

def descuentos_print(sb):
       desc_parafiscal = 0.09
       desc_salud = 0.04
       desc_pension = 0.04
       print(f"Descuento parafiscales: {sb * desc_parafiscal}")
       print(f"Descuento salud: {sb * desc_salud}")
       print(f"Descuento pensión: {sb *desc_pension}")
       print(f"Suma de todos los descuentos: {sb*desc_parafiscal+sb*desc_salud+sb*desc_pension}")
   
def sueldoNeto(sb):
       desc_parafiscal = 0.09 *sb
       desc_salud = 0.04 *sb
       desc_pension = 0.04*sb
       desc_total = desc_parafiscal + desc_salud + desc_pension
       total = sb-desc_total
       print(F"Sueldo Neto: {total}")

def provisiones(sb):
       prov_prima = 0.0833 * sb
       prov_cesantias = 0.0833 *sb
       prov_int_cesantias = 0.01*sb
       prov_vacaciones = 0.0417 *sb
       print(f"Provisiones prima: {prov_prima}")
       print(f"Provisiones Cesantias: {prov_cesantias}")
       print(f"Provisioens Interes Cesantias: {prov_int_cesantias}")
       print(f"Provisiones Vacaciones {prov_vacaciones}")

sueldoBruto_print(ht,vh)
descuentos_print(sb)
sueldoNeto(sb)
provisiones(sb)

 

