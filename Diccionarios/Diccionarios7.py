cantidad = int(input("Ingrese cantidad de vendedores: "))
ventas = {}

for i in range(cantidad):
    nombre = input(f"Nombre del vendedor {i+1}> ")
    total = int(input(f"Total mensual del vendedor {i+1}> "))
    ventas[nombre] = total
   

mejorVendedor = ""
mayor = 0 
for nombre, total in ventas.items():
    if total > mayor:
        mayor = total
        mejorVendedor = nombre
        
print("Mayor vendedor: ")
print(f"{mejorVendedor} -> {mayor}")

#2

cantidad = int(input("Cantidad de vendedores: "))
ventas = {}

for i in range(cantidad):
    nombre = input(f"Nombre del vendedor {i+1}: ")
    total = int(input(f"Total mensual del vendedor {i+1}: "))
    ventas[nombre] = total

mejor = max(ventas, key=ventas.get)
mayor = ventas[mejor]

#print("El estudiante con la mejor nota es:")
#print(f"{max(ventas, key=ventas.get)} -> {ventas[max(ventas, key=ventas.get)]}")

print(f"{mejor} -> {mayor}")
