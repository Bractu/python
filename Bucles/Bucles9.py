numero = int(input("Ingrese un número entero positivo: "))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"El número {numero} no es primo.")
            break
    else:
        print(F"El número {numero} es primo.")
else:
    print(F"El número {numero} no es primo.")
