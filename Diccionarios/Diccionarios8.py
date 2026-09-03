can = int(input("Cantidad de libros: "))
libros = {}

for i in range(can):
    codigo = input(f"Código del libro {i+1}> ")
    titulo = input(f"Título del libro {i+1}> ")
    libros[codigo] = titulo
    
buscar = input("Libro a buscar: ").lower()
for codigo, titulo in libros.items():
    if codigo.lower() == buscar:
        print("Libro Encontrado: ")
        print(f"{codigo}: {titulo}")
        break
else:
    print(f"El código {buscar} no existe")
