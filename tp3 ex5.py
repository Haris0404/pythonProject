x=int(input("Donnez l’heure de début de la location (un entier) ?:"))

y=int(input("Donnez l’heure de fin de la location (un entier) ?: )"))
while y<x:
    print("« Attention ! le début de la location est après la fin ... »")
    x = int(input("Donnez l’heure de début de la location (un entier) ?:"))
    y = int(input("Donnez l’heure de fin de la location (un entier) ?: )"))


while x >24:
    print("« Les heures doivent être comprises entre 0 et 24 ! » ")
    x = int(input("Donnez l’heure de début de la location (un entier) ?:"))
    y = int(input("Donnez l’heure de fin de la location (un entier) ?: )"))

while y> 24:
    print("« Les heures doivent être comprises entre 0 et 24 ! » ")
    x = int(input("Donnez l’heure de début de la location (un entier) ?:"))
    y = int(input("Donnez l’heure de fin de la location (un entier) ?: )"))


while x==y:
    print("« Attention ! l’heure de fin est identique à l’heure de début. » ")
    x = int(input("Donnez l’heure de début de la location (un entier) ?:"))
    y = int(input("Donnez l’heure de fin de la location (un entier) ?: )"))

if y>x and x<=24 and y<=24 and x!=y:

    c=0
    m=0
    for i in range(x,y):
        if 0<=i<=7 or 17<i<=24:
            c=c+1
        if 7<i<=17:
            m=m+1


    z=(c+m*2)
    print("Vous avez loué votre vélo pendant")
    if c!=0:
        print(c,"heure(s) au tarif de horaire de 1.0 euro(s)")
    if m!=0:
        print(m,"heure(s) au tarif de horaire de 2.0 euro(s)")
    print("Le montant total à payer est de ",z,"euro (s).")

