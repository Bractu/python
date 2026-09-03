can = int(input("Cantidad de Empleados: "))
empleados = {}

for i in range(can):
    numero = int(input(f"\nIdentificación del empleado {i+1}> "))
    salario = float(input(f"Salario > "))
    empleados[numero] = salario
    
promedio = sum(empleados.values()) / len(empleados) # O se puede usar can

print(f"Salario promedio: ${promedio:,}")
