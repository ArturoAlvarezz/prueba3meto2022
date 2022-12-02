def crearmatriz(tamaño):
  matriz = []
  for i in range(tamaño):
    matriz.append([])
    for j in range(tamaño):
        matriz[i].append(0)
  return matriz

def marcaralerta(matriz, matriza):
  x=int(input("ingrese la coordenada x: "))
  y=int(input("ingrese la coordenada y: "))
  if(matriz[x][y]==3):
    matriz[x][y]==matriz[x][y]
  else:
    matriz[x][y]=3
  return matriz

print("   menu de dificultad   ")
print("1     principiante    ")
print("2     intermedio   ")
print("3      avanzado   ")
opc = int(input())
matriz=[] 
if(opc==1):
  print("principiante")
  matriz=crearmatriz(9)
  
elif(opc==2):
  print("intermedio")
  matriz=crearmatriz(16)
elif(opc==3):
  print("avanzado")
  matriz=crearmatriz(32)
matriza =matriz

marcaralerta(matriz,matriza)


print(matriz)
