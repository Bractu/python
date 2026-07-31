
#PRIMER MANERA
num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese número 2: "))
num3 = float(input("Ingrese número 3: "))

suma = num1 + num2 + num3
promedio = suma / 3

print(promedio)




#SEGUNDA MANERA
numeros =[]

for i in range(3):
    numero = int(input(f"ingresa el numero {i+1}."))
    numeros.append(numero)

suma= sum(numeros)
promedio = suma/3
print(f"El promedio de los números es : {promedio}")




