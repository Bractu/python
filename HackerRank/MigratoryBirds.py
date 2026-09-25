def migratoryBirds(arr):
    conteo = {}
    for ave in arr:
        if ave in conteo:
            conteo[ave] += 1
        else:
            conteo[ave] = 1
    maxFrecuencia = 0
    mejor = 0
    
    for ave, frecuencia in conteo.items():
        if frecuencia > maxFrecuencia:
            maxFrecuencia = frecuencia
            mejor = ave
        elif frecuencia == maxFrecuencia:
            if ave < mejor:
                mejor = ave
    return mejor