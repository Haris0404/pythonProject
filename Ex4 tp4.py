L1=[2,7,5,6,7,1,6,2,7,6]

a=0
compteur=0
compteur2=0
x=0

for i in range(0, len(L1)):
    for a in range(i+1, len(L1)):
        if L1[i]==L1[a]:
            compteur=compteur+1
    if compteur>compteur2:
        compteur2=compteur
        x=L1[i]
    compteur=0
print("Le nombre le plus frequant est" ,x ,(compteur2+1), "x")