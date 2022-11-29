
print("Tapez 1 si vous souhaitez utiliser la boucle for i inrange")
print("Tapez 2 si vous souhaitez utiliser la boucle for i inrange")
x=int(input("Quel boucle souhaitez-vous utiliser ?: "))
if x== 1:
    nbr = int(input('Entrez un nombre : '))
    fact = 1
    for i in range(1, nbr + 1):
        fact = fact * i
        print(nbr, '! = ', fact)
if x== 2:
    nbr = int(input('Entrez un nombre : '))
    fact = 1
    a=1
    while a<=nbr:
        fact = fact * a
        a= a+1
        print(nbr, '! = ', fact)

