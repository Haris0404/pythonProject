x = int(input("Entrez un nombre entier :"))
if x==0:
    print("le nombre est zéro( et il est pair)")
if x>0:
    if x%2==0:
        print("le nombre est positif et pair")
    else:
         print("le nombre est positif et impair")

if x<0:
    if x%2==0:
          print("le nombre est négatif et pair")
    else:
          print("le nombre est négatif et impair")
