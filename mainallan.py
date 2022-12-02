fila=5
columna=8

a=""

t = []
for i in range(fila):
  t.append([0] * columna)

for k in range(fila):

    for j in range(columna):

       # print(m[k][j])

        a+=str(t[k][j])+'\t'

    print (a)

    a=""