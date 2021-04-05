import random

def dimensions(m):
    return [len(m),len(m[0])]

nbcol=int(random.random()*10)+1      
matrice=[[int(random.random()*100) for i in range(1,nbcol)] for j in range(0,int(random.random()*10)+1)]

print("Matrice")
for i in range (0,len(matrice)):
    print(matrice[i])

dimension=dimensions(matrice)

print("La matrice a",dimension[0],"ligne(s) et",dimension[1],"colonne(s)")