nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
notes = []
note=0
for i in range(0,nombreEtudiants):
    note = float(input("note de l'étudiant",))

    if  note<0 or note> 20:
        print("note non valide")
        note = float(input("Donnez la note de l'étudiant"))
    notes.append(note)
    sum(notes)


moyenne= sum(notes)/nombreEtudiants
print("la moyenne est",moyenne,)
