tamaño = 9
matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(0)

print(matriz)


def comprobarJuego(tamaño):
    seGanaCon = tamaño**2
    contadorParaGanar = 0
    for i in range(filas):
        for j in range(columnas):
            if(matriz[i][j] == 0):
                contadorParaGanar += 1

    if contadorParaGanar == seGanaCon:
        print("Ganaste")