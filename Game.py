import random

def comprobarJuego (tamano, matriz):
    seGanaCon = tamano**2
    contadorParaGanar = 0
    for i in range(filas):
        for j in range(columnas):
            if(matriz[i][j] == 0):
                contadorParaGanar += 1

    if contadorParaGanar == seGanaCon:
        print("Ganaste")

def crearmatriz(tamaño):
  matriz = []
  for i in range(tamaño):
    matriz.append([])
    for j in range(tamaño):
        matriz[i].append(0)
  return matriz


print("   menu de dificultad   ")
print("1     principiante    ")
print("2     intermedio   ")
print("3      avanzado   ")
opc = int(input())
matriz=[]
if(opc==1):
    tamano = 9
    print("principiante")
    matriz=crearmatriz(tamano)
  
elif(opc==2):
    tamano = 16
    print("intermedio")
    matriz=crearmatriz(tamano)
elif(opc==3):
    tamano = 32
    print("avanzado")
    matriz=crearmatriz(tamano)

def menuDeJuego():
    print("bienvenido al menu de juego buscaCovid")
    print("seleccione si quiere jugar o reiniciar el juego")
    i=0
    while i<10:
        x = int(input("pulse [1] para iniciar pulse [2] para reiniciar \n"))
        if (x==1):
            print("seleccionó iniciar partida")
            i=12
        if (x==2):
            print("Selecionó reiniciar partida")
            i=12
    

r=[]
for i in range(tamano):
  r.append([0] * tamano)

for k in range(tamano):
  for j in range(tamano):
    r[k][j]=random.randint(0,1)


def imprimirmatriz(tamano, t):
  a=""
  for k in range(tamano):

    for j in range(tamano):
      a+=str(t[k][j])+'\t'

    print (a)
    a=""
def desbloquearcasilla():
  x=int(input("ingrese la coordenada x: "))
  y=int(input("ingrese la coordenada y:"))
  t[x][y]=r[x][y]
  
juego = 1

while juego != 1:
    imprimirmatriz(tamano, matriz)
    comprobarJuego(tamano, matriz)
    print("\n")
    print("1 para menu de juego,2 para ingresar coordenadas")
    opcion = int(input())
    if opcion == 1:
        menuDeJuego()
    elif opcion == 2:
        desbloquearcasilla()
        


