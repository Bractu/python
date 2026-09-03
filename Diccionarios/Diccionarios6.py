cantidad = int(input("Ingrese cantidad de estudiantes: "))
estudiantes = {}

for i in range(cantidad):
    estudiante = input(f"Nombre del estudiante {i+1}> ")
    nota = float(input(f"Nota del estudiante {i+1}> "))
    estudiantes[estudiante] = nota
   

mejorEstudiante = ""
mayor = -1 
for nombre, nota in estudiantes.items():
    if nota > mayor:
        mayor = nota
        mejorEstudiante = nombre
        
print("El estudiante con la mejor nota es: ")
print(f"{mejorEstudiante} -> {mayor}")
