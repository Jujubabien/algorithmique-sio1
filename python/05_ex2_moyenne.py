nbnotes=int(input("veuillez saisir le nombre de notes: "))
tab=[]

for i in range(1, nbnotes+1):
    tab.append(float(input("saisir la note N°"+str(i)+": ")))

total=0
for i in range(0, nbnotes):
    total+=tab[i]

moyenne=total/nbnotes
print("La moyenne des notes est: "+str(moyenne))

