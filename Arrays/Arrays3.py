cant = int(input("cantidad de números a ingresar: "))

pares = []
impares = []

for i in range(cant):
    num = int(input("Ingrese un numero entero: "))
    i += 1
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
print(impares, pares)
