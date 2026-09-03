def restar(saldo,retirar):
    return(saldo-retirar)
def sumar(saldo,depositar):
    return(saldo+depositar)
def menu():
    print("Seleccione una opción")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    print("-"*40)

saldo = 0
validador = False
claveCorrecta = "2002"
contador = 0
while True:
    clave = input("Ingrese su clave> ")
    if clave == claveCorrecta:
        print("Entraste al menú principal")
        validador = True
    elif clave != claveCorrecta:
        print("Clave incorrecta, ingresa de nuevo")
        contador += 1
        if contador == 3:
            print("Intentos fallidos, cerrando...")
            break

        
    while validador == True:
        menu()
        opcion = int(input("Seleccione una opción (1-5): "))
        match opcion:
            case 1:
                print(f"Has elegido Consultar saldo")
                print(f"El saldo disponible es: ${saldo:,}")
                print("-"*40)
            case 2:
                print("Has elegido Depositar dinero")
                depositar = int(input("Cuanto desea depositar: "))
                saldo = sumar(saldo,depositar)
                print(saldo)
                print("-"*40) 
            case 3:
                print("Has elegido Retirar dinero")
                retirar = int(input("Cuanto desea retirar"))
                if saldo < retirar:
                    print("Saldo insuficiente")
                    print("-"*40)
                else:
                    saldo = restar(saldo,retirar)
                    print(f"Ha retirado ${retirar} y su saldo diponible es ${saldo}")
                    print("-"*40)
                    break
            case 4:
                print("Has elegido Salir")
                print("-"*40)
                break
            case _:
                print("Opción no válida")
                print("-"*40)
            
            
             


