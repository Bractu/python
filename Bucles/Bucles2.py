num = int(input("Ingrese un numero entero: "))
pares = []

for i in range(num):
    i += 1
    if i % 2 == 0:
        pares.append(i)
    
print(*pares)
