cantidad = int(input("Dame el numero de valores a ingresar: "))

numeros = []

for i in range(cantidad):
    num = input(f"Ingrese el valor {i+1}: ")
    numeros.append(num)
    
mayor = numeros[0]
menor = numeros[0]
    
for num in numeros:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
        
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
