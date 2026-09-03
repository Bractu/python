cantidad = int(input("Ingrese cantidad de la lista > "))

lista1 = []
lista2 = []

for i in range(cantidad):
    num1 = int(input(f"Ingrese el numero {i+1} de la primer lista: "))
    lista1.append(num1)
    
for i in range(cantidad):
    num2 = int(input(f"Ingrese el numero {i+1} de la segunda lista: "))
    lista2.append(num2)
    
combinada = lista1 + lista2
print(combinada)
