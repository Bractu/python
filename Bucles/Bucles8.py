palabra = input("Ingrese la palabra: ")
vocales = ("a", "e", "i", "o", "u")
texto = palabra.lower()
cont = 0
for letra in texto:
    for vocal in vocales:
        if letra == vocal:
            cont += 1
        
print(f"La palabra tiene {cont} vocales.")
