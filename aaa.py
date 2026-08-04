cilindro1 = int(input("Ingrese la compresión del cilindo 1 en PSI: "))
cilindro2 = int(input("Ingrese la compresión del cilindo 2 en PSI: "))

compresion = [cilindro1, cilindro2]
suma = sum(compresion)
prom = suma/2

if prom < 110:
    print(f"Compresión baja ({prom}): El motor necesita reparación")
else:
    print(f"Compresión óptima ({prom}): Motor en buen estado")