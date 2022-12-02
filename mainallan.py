fila=8
columna=8



t = []
for i in range(fila):
  t.append([0] * columna)
def imprimirmatriz(tamano):
  a=""
  for k in range(tamano):

    for j in range(tamano):
      a+=str(t[k][j])+'\t'

    print (a)

    a=""
def desbloquearcasilla():
  x=int(input("ingrese la coordenada x: "))
  y=int(input("ingrese la coordenada y: "))
  t[x][y]=1
desbloquearcasilla()
imprimirmatriz(8)
