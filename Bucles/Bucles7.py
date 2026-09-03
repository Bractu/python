num = int(input("Ingrese un numero entero: "))
impares = []

for i in range(num):
    i += 1
    if i % 2 != 0:
        impares.append(i)

suma = sum(impares)
print(f"La suma de los números impares es: {suma}")
