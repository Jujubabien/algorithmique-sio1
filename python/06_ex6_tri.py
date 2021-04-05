import random

def tri(m):
    # algorithme du tri à bulle
    for i in range(len(m)-1,0,-1):
        for j in range(0,i):
            if m[j+1]<m[j]:
                m[j+1],m[j] = m[j],m[j+1]


    return m

    
liste=[int(random.random()*100) for i in range(0,int(random.random()*20)+1)]

print("Liste")
print(liste)
print("Liste triée")
listetriee=tri(liste)
print(listetriee)