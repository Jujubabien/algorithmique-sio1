somme=0
i=0
while i<100:
    somme+=i
    i+=2
print("la somme des nombres pairs strictement inférieurs à 100 est",somme)

# pour rappel : 
# Gauss a établi que la somme des nombres entiers jusqu'à n = (n*(n+1))/2
# somme des entiers pairs jusqu'à 2n = 2 * somme des entiers jusqu'à n soit n*(n+1)
# dans notre cas (nombres pairs < 100) 2n=98, donc n=49, somme des pairs jusqu'à 100 = 49*50 soit 2450