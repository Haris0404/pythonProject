p=0
j=0
k=0
for i in range(0,10):
    x = int(input("Entrez x :"))

    while x > 20 and x< 0:
        x = int(input("Entrez x :"))
    if x <10:
        p = p+1
    if x >=15:
        j = j+1
    if  10 <= x <15:
        k=k+1

print("Le nombre de valeurs inférieur strictement  à 10 est :",p )
print("Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est :",k)
print("Le nombre de valeurs supérieur ou égale à 15 est:",j)






