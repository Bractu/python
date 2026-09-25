def sumar(num1,num2):
    return(num1+num2)
def restar(num1,num2):
    return(num1-num2)
def multiplicar(num1,num2):
    return(num1*num2)
def dividir(num1,num2):
    return(num1/num2)

while True:
    num1 = float(input("Ingrese el primer número > "))
    num2 = float(input("Ingrese el segundo número > "))
    print("""         MENÚ
        1: SUMA 
        2: RESTA 
        3: MULTIPLICACION 
        4: DIVISION""")
    
    opcion = int(input("Escoge la opcion: "))
    if opcion == 1:
        print("Has escogido Suma")
        suma = sumar(num1,num2)
        print(suma)
    if opcion == 2:
            print("Has escogido Restar")
            resta = restar(num1,num2)
            print(resta)
    if opcion == 3:
            print("Has escogido Multiplicar")
            multi = multiplicar(num1,num2)
            print(multi)
    if opcion == 4:
            print("Has escogido División")
            division = dividir(num1,num2)
            print(division)
    if opcion == 5:
            print("Has escogido Finalizar")
            break