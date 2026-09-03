can = int(input("Ingrese cantidad de productos: "))
inventario = {}

for i in range(can):
    producto = input(f"Ingrese el producto  {i+1}> ")
    cantidad = int(input(f"Cantidad del producto {i+1}> "))
    inventario[producto] = cantidad
    
buscar = input("Producto a buscar: ").lower()
for producto, cantidad in inventario.items():
    if producto.lower() == buscar:
        print(f"Cantidad disponible de {producto}: {cantidad}")
    else:
        print("Producto inexxistente")
