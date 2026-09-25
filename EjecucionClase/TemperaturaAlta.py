semana = {
    "lunes" : [],
    "martes" : [],
    "miercoles" : [],
    "jueves" : [],
    "viernes" : [],
    "sabado" : [],
    "domingo" : [] 
}
for dia in semana:
    temp = float(input(f"Ingrese la temperatura del {dia} > "))
    print("-"*50)
    semana[dia] = temp

prom = sum(semana.values()) / len(semana)
alta = max(semana.values())
baja = min(semana.values())
cont = 0
i = 0
for dia in semana:
    if semana[dia] > prom:
        cont += 1

print("~"*50)
print(f"Temperatura mas alta registrada: {alta} \nTemperatura mas baja registrada: {baja} \nLa temperatura promedio: {prom} \nLo dias con temperatura por encima del promedio: {cont}")
print("~"*50)

    


