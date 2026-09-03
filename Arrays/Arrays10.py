cantidad = int(input("Ingrese cantidad de numeros de la lista: "))
compras = []

for i in range(cantidad):
    producto = input(f"Ingrese el producto {i+1} > ")
    compras.append(producto)
    
for i in range(len(compras)):
    
    print(f"{i+1}. {compras[i]}")
