notas = [3.5, 4.0, 4.2, 5.0]
suma = 0 
cont = 0

for i in notas:
    suma += i
    cont += 1
    
prom = suma / cont
    
print(round(prom, 2))

#2

notas = [3.5, 4.0, 4.2, 5.0]
cont = 0
suma = sum(notas)
for i in notas:
    cont += 1
    
prom = suma / cont
    
print(round(prom, 2))
