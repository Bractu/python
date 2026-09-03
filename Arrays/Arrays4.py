cantidad = int(input("Ingrese cantidad de la lista > "))
buscar = int(input("Ingrese el número a buscar > "))
numeros = []
for i in range(cantidad):
    num = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(num)
  
#for i in range(cantidad):
    

if buscar in numeros:
    print(f"El número {buscar} se encuentra en la posición {numeros.index(buscar)} de la lista")
else:
    print(f"El número {buscar} se encuentra en la lista")

