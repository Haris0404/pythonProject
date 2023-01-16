person1 = input("Entrez le nom et le prénom de la première personne (séparé par un espace) : ").split()
person2 = input("Entrez le nom et le prénom de la deuxième personne (séparé par un espace) : ").split()

person1[0] = person1[0].upper()
person1[1] = person1[1].capitalize()
person2[0] = person2[0].upper()
person2[1] = person2[1].capitalize()

if (person1[0] + person1[1] > person2[0] + person2[1]):
    person1, person2 = person2, person1

print(f"{person1[1]} {person1[0]}")
print(f"{person2[1]} {person2[0]}")