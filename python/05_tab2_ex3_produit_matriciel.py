nblignes1=int(input("veuillez saisir le nombre de lignes de la matrice 1: "))
nbcolonnes1=int(input("veuillez saisir le nombre de colonnes de la matrice 1: "))

nblignes2=nbcolonnes1
print("la matrice 2 aura ",nbcolonnes1,"lignes")
nbcolonnes2=int(input("veuillez saisir le nombre de colonnes de la matrice 2: "))



a=range(nblignes1)  
b=range(nbcolonnes1) 
c=range(nbcolonnes2)

matrice1=[[0 for i in b] for j in a]
matrice2=[[0 for i in c] for j in b]


print("saisie de la matrice 1")
for i in range (0,nblignes1):
    print("saisie de la ligne",i+1)
    for j in range (0,nbcolonnes1):
        matrice1[i][j]=int(input("Saisissez la valeur de la colonne "+str(j+1)+" pour la ligne "+str(i+1)+": "))


print("saisie de la matrice 2")
for i in range (0,nblignes2):
    print("saisie de la ligne",i+1)
    for j in range (0,nbcolonnes2):
        matrice2[i][j]=int(input("Saisissez la valeur de la colonne "+str(j+1)+" pour la ligne "+str(i+1)+": "))


produit=[[0 for i in c] for j in a]

for i in a:
    for j in c:
        for k in b:
            produit[i][j]+=matrice1[i][k]*matrice2[k][j]



print("Matrice 1")
for i in range (0,len(matrice1)):
    print(matrice1[i])

print("Matrice 2")
for i in range (0,len(matrice2)):
    print(matrice2[i])

print("Matrice 1 * Matrice 2")
for i in range (0,len(produit)):
    print(produit[i])