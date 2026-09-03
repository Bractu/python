cantidad = int(input("Ingrese cantidad de palabras > "))

lista = []
invertida = []
for i in range(cantidad):
    palabras = input(f"Ingrese la palabra {i+1}: ")
    lista.append(palabras)
    
for i in lista[::-1]:
    invertida.append(i)
    
print(*invertida)
    

