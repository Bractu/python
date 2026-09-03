cantidad = int(input("Ingrese cantidad de contactos: "))
guia = {}

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del contacto {i+1}> ")
    numero = int(input(f"Número de teléfono del contacto {i+1}> "))
    guia[nombre] = numero
    
buscar = input("Ingrese el nombre a buscar: ").lower()
for nombre, numero in guia.items():
    if nombre.lower() == buscar:
        print(f"Teléfono de {nombre} : {numero}")
    else:
        print("Contacto inexistente")
