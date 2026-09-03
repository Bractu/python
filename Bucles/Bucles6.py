cantidad = int(input("Indique cantidad de numeros a ingresar: "))
num = {
    "positivos" : [],
    "negativos" : [],
    "ceros" : []
}
ingresados = []
for i in range(cantidad):
    numeros = float(input(f"Ingrese el numero {i+1}: "))
    ingresados.append(numeros)

for i in range(cantidad):
    if ingresados[i] > 0:
        num["positivos"].append(ingresados[i])
    elif ingresados[i] < 0:
        num["negativos"].append(ingresados[i])
    else:
        num["ceros"].append(ingresados[i])
            
for clave, valor in num.items():
    print(f"{clave} : {len(valor)}")

