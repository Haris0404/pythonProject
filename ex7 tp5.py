import os
import time

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

if not os.path.exists(fichier1) or not os.path.exists(fichier2):
    print("Au moins un des fichiers n'existe pas.")
else:
    size1 = os.path.getsize(fichier1)
    size2 = os.path.getsize(fichier2)
    mod_time1 = os.path.getmtime(fichier1)
    mod_time2 = os.path.getmtime(fichier2)

    print("Taille du premier fichier :", size1, "octets")
    print("Taille du deuxième fichier :", size2, "octets")

    if mod_time1 > mod_time2:
        print("Le premier fichier est le plus récent.")
        print("Date de modification: ",time.ctime(mod_time1))
    elif mod_time2 > mod_time1:
        print("Le deuxième fichier est le plus récent.")
        print("Date de modification: ",time.ctime(mod_time2))
    else:
        print("Les fichiers ont la même date de modification.")