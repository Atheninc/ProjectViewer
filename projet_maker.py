import json
import sys

filename = sys.argv[1]

projet = input("Entrez le nom du projet: ")
description = input("Entrez une description du projet: ")
tache = []

while True:
    nom_tache = input("Entrez le nom de la tâche: ")
    priorite = input("Entrez la priorité de la tâche (haute, moyenne, basse): ")
    responsable = input("Entrez le responsable de la tâche: ")
    sous_tache = []
    
    while True:
        nom_sous_tache = input("Entrez le nom de la sous-tâche: ")
        if len(nom_sous_tache) == 0:
            break
        else:
            sous_tache.append(nom_sous_tache)
            
    tache.append({"nom": nom_tache, "priorite": priorite, "responsable": responsable, "sous_tache": sous_tache})
    
    cont = input("Continuer à ajouter des tâches (y/n)? ")
    if cont.lower() != 'y':
        break
        
data = {"projet": projet, "description": description, "tache": tache}

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
 

print("Le fichier JSON a été créé avec succès!")
