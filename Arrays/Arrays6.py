numeros = []
sinRepetir = []
i=0
while True:
    num = int(input(f"Ingrese el numero {i+1}> "))
    numeros.append(num)
    i+=1
    if i % 5 == 0:
        entrada = input("Parammos?: ")
    
        if entrada == "si":
            break
        
for n in numeros:
    if n not in sinRepetir:
        sinRepetir.append(n)
        
print(sinRepetir)

