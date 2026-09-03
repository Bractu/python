num = int(input("Ingrese un numero entero: "))

for i in range(num, 1, -1):
    i-= 1
    num = num * i
   

print(num)
