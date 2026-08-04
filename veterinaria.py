print("FACTURACIÓN VETERINARIA")
propietario = input("Nombres Propietario: ")
mascota = input("Nombre Mascota: ")
valorConsulta = float(input("Valor de la consulta: $"))
valorMedicamentos = float(input("Valor de medicamentos o exámenes: "))

iva = 0.19
subtotal = valorConsulta + valorMedicamentos
valorIva = subtotal * iva
total = subtotal + valorIva

print("==============================")
print("   FACTURA SERVICIO PRESTADO   ")
print("==============================")
print(f"PROPIETARIO: {propietario}")
print(f"MASCOTA: {mascota}")
print("==============================")
print(f"VALOR CONSULTA: {valorConsulta:,.0f}")
print(f"VALOR MEDICAMENTOS: {valorMedicamentos:,.0f}")
print(f"SUBTOTAL: {subtotal:,.0f}")
print(f"IVA 19%: {valorIva:,.0f}")
print("==============================")
print(f"TOTAL A PAGAR: {total:,.0f}")
print("==============================")