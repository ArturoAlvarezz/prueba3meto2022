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

