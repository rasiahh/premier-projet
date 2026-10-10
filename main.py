taches = []
choix = 0
sortie = False
while not sortie:
    choix=int(input("Choisissez une option: \n1. Ajouter une tâche \n2 Supprimer une tâche \n3. Afficher les tâches \n4. Arrêter le programme"))
    while choix>4 or choix<=0:
        choix=int(input("Choisissez une option: \n1. Ajouter une tâche \n2 Supprimer une tâche \n3. Afficher les tâches \n4. Arrêter le programme"))
    if choix == 1:
        taches.append(input("Entrez la tâche à ajouter:"))
    elif choix==2:
        if len(taches)!=0:
            suppr = int(input("Entrez le numéro de la tâche à supprimer:"))-1
            while suppr<0 or suppr>=len(taches):
                suppr = int(input("Entrez le numéro de la tâche à supprimer:"))-1
            taches.pop(suppr)
        else:
            print("Aucune tâche à supprimer...")
    elif choix==3:
        if len(taches)!=0:
            for i in range(len(taches)):
                print(f"{i+1}. {taches[i]}")
        else:
            print("Aucune tâche à afficher...")
    else:
        sortie=True
