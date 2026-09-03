cantidad = int(input("Ingrese cantidad de la lista > "))

numeros = []

for i in range(cantidad):
    num = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(num)
    
for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    

print(numeros)

