import random
x=int(input("Devinez la valeur de X : "))
z= random.randint(0, 100)
c=0
while x!=z:
    c=c+1
    if z<x:
        print("la valeur est plus petite")
        x = int(input("Entrez une valeur plus petite : "))
    if z>x:
        print("la valeur est plus grande")
        x = int(input("Entrez une valeur plus grande : "))

print("Vous avez trouvez la bonne valeur de X avec ", c, "essais ")





