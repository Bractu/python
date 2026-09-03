cantidad = int(input("Ingrese cantidad de numeros de la lista: "))
numeros = []

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1} > "))
    numeros.append(num)

numeros.sort()

mayor = numeros[-1]
segundoMayor = numeros[0]
for i in numeros:
    if i < mayor and i > segundoMayor:
        segundoMayor = i

print(segundoMayor)
