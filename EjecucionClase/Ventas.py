cantDias = int(input("Ingrese cantidad de dias que desea registrar: "))
dias = []
for i in range(cantDias):
    ventas = float(input(f"Ingrese la venta del día {i+1} > "))
    print("-"*50)
    dias.append(ventas)

prom = sum(dias) / len(dias)
alta = max(dias)
baja = min(dias)
total = sum(dias)
cont = 0

for c in range(len(dias)):
    if dias[c] > prom:
        cont += 1

print("~"*50)
print(f"Venta mas alta: ${alta:,.0f} \nVenta mas baja: ${baja:,.0f} \nTotal vendido: ${total:,.0f} \nVenta promedio: ${prom:,.0f} \nLo dias en la que la venta estuvo por encima del promedio: {cont}")
print("~"*50)
