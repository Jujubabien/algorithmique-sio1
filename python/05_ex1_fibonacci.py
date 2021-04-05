nterms = int(input("Entrez le nombre de termes de la suite: "))

 
tab=[0]
tab.append(1)

for i in range(2, nterms):
  tab.append(tab[i-1] + tab[i-2])
  
print(tab)