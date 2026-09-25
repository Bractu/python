def menu():
    print("Menu de elecciones")
    print("1. Registrar deportista")
    print("2. Mostrar deportistas")
    print("3. Buscar deportista")
    print("4. Mostrar mejor tiempo")
    print("5. Mostrar tiempo promedio")
    print("6. Salir")

nombres = []
tiempos = []

while True:
        menu()
        opcion = int(input("Seleccione una opción (1-5): "))
        match opcion:
            case 1:
                print("Elegiste registrar deportistas")
                nombre = input("Ingrese el nombre del deportista: ")
                print("-"*50)
                nombres.append(nombre)
                tiempo = float(input("Ingrese el tiempo del deportista en segundos: "))
                print("-"*50)
                tiempos.append(tiempo)
            case 2:
                print("Elegiste mostrar deportistas")
                for i in range(len(nombres)):
                    if i != 0:
                        print(f"{nombres[i]} : {tiempos[i]}")
                    else:
                        print("No hay deportistas registrados")
            case 3:
                print("Elegiste buscar deportista")
                buscar = input("Nombre del deportista a buscar: ")
                for i in range(len(nombres)):
                    if buscar == nombres[i]:
                        print(buscar,tiempos[i] )
                    elif len(nombres) == 0:
                        print("No existe el deportista")
            case 4:
                print("Elegiste mostrar mejor tiempo")
                mejor = min(tiempos)
                pos = tiempos.index(mejor)
                if mejor > 0:
                    print( nombres[pos],mejor)
                else:
                    print("No hay tiempos registrados")
            case 5:
                print("Elegiste mostrar tiempo promedio")
                prom = sum(tiempos) / len(tiempos)
                if prom > 0:
                    print(prom)
                else:
                    print("No hay deportistas registrados")
            case 6:
                print("Elegiste Salir")
                exit()