dict = {}

nom = input("Entrez votre prénom : ")
prenom= input("Entrez votre nom : ")
promo = input("Entrez votre promotion : ")
groupe = input("Entrez votre groupe de TP : ")

dict["nom"] = nom
dict["prenom"] = prenom
dict["promo"] = promo
dict["groupe"] = groupe

for key, value in dict.items():
    print(f"{key} : {value}")