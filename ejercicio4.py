numero = int(input("Ingrese un número de 2 dígitos: "))

#decenas = numero//10  #Division enteraaa
#unidades = numero%10

decenas = int(numero/10)
unidades = numero - (decenas*10) 
print(f"Las unidades de tu número son: {unidades} y las decenas son: {decenas}")