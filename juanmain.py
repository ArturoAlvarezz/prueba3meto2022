print("bienvenido al juego buscaCovid")
print("seleccione si quiere jugar o reiniciar el juego")
print("Iniciar juego")
i=0
while i<10:
  x=int(input("pulse [1] para iniciar pulse [2] para reiniciar \n"))
  if (x==1):
    print("seleccionó iniciar partida")
    i=12
  if (x==2):
    print("Selecionó reiniciar partida")
    i=12
    

import random

fila=8
columna=8

t = []
r=[]
for i in range(fila):
  t.append([0] * columna)
for i in range(fila):
  r.append([0] * columna)

for k in range(fila):
  for j in range(fila):
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
  
desbloquearcasilla()
imprimirmatriz(8, t)
print("\n")
imprimirmatriz(8, r)



def recorrematriz(tamano,t):
  a=0
  b=0
  puntos= 0
  while a<=63 and b<=63:
    if (r[a][b]==1):
      puntos=puntos+1
      print(r[a][b])
      if (x==8 or x==16 or x==32 or x==40 or x==48)
      b=b+1
    a=a+1
    

  
  print("puntos: ",puntos)
recorrematriz(8,r)
