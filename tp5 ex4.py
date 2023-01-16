argent = int(input("Entrez une somme d'argent : "))
euro=argent
b100 = argent // 100
argent = argent % 100

b50 = argent // 50
argent = argent % 50

b10 = argent // 10
argent = argent % 10

p2 = argent // 2
argent = argent % 2

p1 = argent // 1

print(euro,"euros, c'est donc ",b100, "billets de 100",b50, "billets de 50",b10,"billets de 10",p2,"pièces de 2 et ",p1, "pièces de 1.")