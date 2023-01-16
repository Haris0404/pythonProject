heures = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

if heures <= 160:
    salaire = heures * salaire_horaire
elif heures <= 200:
    salaire = 160 * salaire_horaire + (heures - 160) * salaire_horaire * 1.25
else:
    salaire = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (heures - 200) * salaire_horaire * 1.5

print("Le salaire de l'ouvrirer est",salaire,"euros")