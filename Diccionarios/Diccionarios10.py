cantidad = int(input("Cantidad de estudiantes: "))
estudiantes = {}

for i in range(cantidad):
    print(f"Estudiante {i+1}:")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    promedio = float(input("Promedio: "))

    estudiantes[codigo] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }
    
mejorCodigo = ""
mayor = -1
for codigo, informacion in estudiantes.items():
    if informacion["promedio"] > mayor:
        mayor = informacion["promedio"]
        mejorCodigo = codigo

print("\nMejor estudiante")
print(f"Código: {mejorCodigo}")
print(f"Nombre: {estudiantes[mejorCodigo]["nombre"]}")
print(f"Edad: {estudiantes[mejorCodigo]["edad"]}")
print(f"Carrera: {estudiantes[mejorCodigo]["carrera"]}")
print(f"Promedio: {estudiantes[mejorCodigo]["promedio"]}")
