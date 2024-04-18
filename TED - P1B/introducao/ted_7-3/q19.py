import math

coordenadas = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

distancia_total = 0

for i in range(len(coordenadas) - 1):

    distancia = math.sqrt((coordenadas[i+1][0] - coordenadas[i][0]) ** 2 + 
                          (coordenadas[i+1][1] - coordenadas[i][1]) ** 2 + 
                          (coordenadas[i+1][2] - coordenadas[i][2]) ** 2)
    
    distancia_total += distancia

print("Distância total percorrida:", distancia_total)
