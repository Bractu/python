cant = int(input("Cantidad de atletas que participaron: "))
tiempos = []

for i in range(cant):
    time = float(input(f"Ingrese el tiempo del atleta {i+1} en seg. > "))
    tiempos.append(time)
    
prom = sum(tiempos) / len(tiempos)
peor = max(tiempos)
mejor = min(tiempos)
total = sum(tiempos)
cont = 0

for c in range(len(tiempos)):
    if tiempos[c] < prom:
        cont += 1
        print(cont)
        
print("*"*40)
print(f"* Mejor tiempo: {mejor} s")
print(f"Peor tiempo: {peor} s")
print(f"Tiempo promedio: {prom:.2f} s")
print(f"Atletas pro debajo del promedio: {cont} s")
print("*"*40)



