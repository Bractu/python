cantidad = int(input("Ingrese cantidad de estudiantes: "))
estudiantes = {}

for i in range(cantidad):
    codigo = int(input(f"Ingres el codigo del estudiante {i+1}> "))
    nombre = input(f"Nombre del estudiante {i+1}> ")
    estudiantes[codigo] = nombre
    
for codigo, nombre in estudiantes.items():
    print(f"{codigo} -> {nombre}")
