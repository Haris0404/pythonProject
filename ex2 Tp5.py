notes = []
coefficients = []
somme_coefficients = 0
somme_notes = 0

for i in range(5):
    note, coefficient = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant (séparé par un espace) : ").split()
    notes.append(float(note))
    coefficients.append(int(coefficient))
    somme_coefficients += coefficients[i]
    somme_notes += notes[i] * coefficients[i]

moyenne = somme_notes / somme_coefficients

moyenne=int(moyenne)
note=int(note)
if moyenne>10 and note>8:
    print("L'étudiant est admis")
else:
    print("L'étudiant n'est pas admis")

print(f"La moyenne est de ",moyenne)