tab=[]

for i in range(0, 10):
    tab.append(int(input(str(i+1)+" - saisir un nombre: ")))

print(tab)

tab2=[]
for i in range (0,10):
    tab2.append(tab[len(tab)-i-1])

print(tab2)
  