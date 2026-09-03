frase = input("Ingrese la frase: ")

dividida = {}

for letra in frase:
    if letra != " ":
        if letra in dividida:
            dividida[letra] += 1
        else:
            dividida[letra] = 1
        
for letra, veces in dividida.items():
    print(f"{letra} : {veces}")

