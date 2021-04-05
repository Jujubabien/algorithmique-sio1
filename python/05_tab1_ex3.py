tab1=[7,19,23,4,9,22,11]
tab3=tab1
tab2=[]
for i in range(0, len(tab1)):
   tab2.append(tab1[i])

tab1[0]=8
print(tab1)
print(tab2)
print(tab3)