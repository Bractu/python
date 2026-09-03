cantidad = int(input("Ingrese la cantidad de términos: "))
serie = [0, 1]

for i in range(cantidad-2):
    siguiente = serie[-1] + serie[-2]
    serie.append(siguiente)
    
print(serie)
