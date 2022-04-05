import random
velocidad_caballo=[]
for i in range(0,25):
    n=random.randint(1,100)
    velocidad_caballo.append(n)
print("lista de caballos y velocidades")
print(velocidad_caballo)

print("\nGrupos desordenados")

grupos=[[],[],[],[],[]]
k=0
for j in range(0,5):
    for i in range(0,5):
        grupos[j].append(velocidad_caballo[k])
        k=k+1
    print(grupos[j])
k=k+5

print("\nGrupos ordenados, 5 carreras")

for j in range(0,5):
    grupos[j].sort()
    print(grupos[j])

for j in range(1,5):
    gpoactual=grupos[j]
    actual=grupos[j][4]
    i=j
    while i>0 and grupos[i-1][4]>actual:
        grupos[i]=grupos[i-1]
        i=i-1
    grupos[i]=gpoactual

print("\nGrupos ordenados por caballo mas rapido, sexta carrera")
for j in range(0,5):
    print(grupos[j])

print("\nSeptima carrera")
ult_grupo.sort(reverse=True)
ult_grupo=[grupo[3][3], grupos[3][4],grupos[4][2], grupos[4][3], grupos[4][4]]
print ("caballos mas veloces: ")
print(ult_grupo[0],ult_grupo[1])

print("\Comprobacion")
print("Lista de 25 sorteada")
velocidad_caballo.sort(reverse=True)
print(velocidad_caballo)
print("caballos mas veloces: ")
print(velocidad_caballo[0], velocidad_caballo[1])
