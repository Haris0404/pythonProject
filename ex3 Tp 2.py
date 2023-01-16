a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
"""      *******************************************
         * Completez le programme a partir d'ici.
         *******************************************
"""
y=b
x=c

b=a
c=y
a=x


"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)