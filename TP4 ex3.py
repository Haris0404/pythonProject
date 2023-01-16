nMax=3
n=0
v1=[]
v2=[]
n=int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))
if n >= 1 and n <= nMax:
    pass
else:
    n=int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))

for i in range(0,3):
    v1.append(int(input("Saisie du premier vecteur ")))

for i in range(0,3):
    v2.append(int(input("Saisie du second vecteur ")))

scale=v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print("Le produit scalaire de v1 par v2 vaut",scale,)



