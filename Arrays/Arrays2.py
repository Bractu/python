cantidad = int(input("cantidad de notas a ingresar: "))

notas   = []

for i in range(cantidad):
    nota = float(input(f"Ingrese el valor {i+1}: "))
    notas.append(nota)
    
suma = sum(notas) 
prom = suma / cantidad
print(f"Promedio: {prom}")
