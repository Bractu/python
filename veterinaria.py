nombreCliente = input("Ingrese el nombre del cliente: ")
serviciosOfrecidos = {
    "limpieza" : 50000,
    "vacunacion" :  20000,
    "desparasitacion" : 50000,
    "revisionFisica" : 100000
}

serviciosRealizados = []
total = 0

print("-----¡Servicios Disponibles!-----")
for servicio, precio in serviciosOfrecidos.items():
    print(f"* {servicio} : {precio}")
print("Ingrese los servicios prestados (escriba fin para generar factura)")

while True:
    entrada = input("> ")
    if entrada == "fin":
        break
    
    if entrada in serviciosOfrecidos:
        precio = serviciosOfrecidos[entrada]
        serviciosRealizados.append((entrada, precio))
        total+= precio
        print(f"servicio {entrada} agregado {precio}")
    else:
        print("El servicio no esta en la lista. ingrese de nuevo")
iva = total * 0.19      
totalConIva = total + iva

print("--------FACTURA DE VENTA--------")
print("--------------------------------")
print(f"CLIENTE: {nombreCliente}.")
    
if serviciosRealizados:
    for servicio, precio in serviciosRealizados:
        print(f" * {servicio} ---------- ${precio}")
    print(f"${totalConIva}.")
    