frase = input("Ingrese la frase: ")

palabras = frase.split()
dividida = {}

for palabra in palabras:
    if palabra in dividida:
        dividida[palabra] += 1
    else:
        dividida[palabra] = 1
        
for palabra, veces in dividida.items():
    print(f"{palabra} : {veces}")

