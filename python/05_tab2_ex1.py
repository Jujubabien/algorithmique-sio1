tab=[[7,22,12,18],[11,32,15,9],[1,4,19,23],[6,3,34,91],[59,24,61,17]]


for i in range (0,len(tab)):
    print(tab[i])

somme=0
for i in range (0,len(tab)):
    for j in range (0,len(tab[i])):
        somme+=tab[i][j]

print("la somme des termes de la matrice est : "+str(somme))

for i in range (0,len(tab)):
    del tab[i][1]


for i in range (0,len(tab)):
    print(tab[i])

tab2=[]
for i in range (0,len(tab)):
    if (i==3):
        tab2.append([2,4,6])
    tab2.append(tab[i])

print("Tableau modifié")
for i in range (0,len(tab2)):
    print(tab2[i])