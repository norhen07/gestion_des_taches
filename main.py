print("=== GESTION DES TÂCHES ===")
list1=['1.Ajouter', '2.Afficher', '3.Rechercher', '0.Quitter']
print(list1)
taches=[]
ch=-1
while ch!=0:
    ch=int(input("Saisir votre choix ="))
    while ch not in [0,1,2,3]:
        ch=int(input("Saisir votre choix ="))
    if ch==1:
        tit=input("saisir un titre =")
        while tit=="":
            print("Le titre ne doit pas etre vide !")
            tit=input("saisir un titre =")
        taches.append(tit)
        print("Tache ajoutee avec succes.")
    elif ch==2:
        if taches==[]:
            print("Aucune tache disponible.")
        else:
            print(taches)
    elif ch==3:
        mot=input("Saisir un mot-cle : ")
        trouve= False
        for i in range(len(taches)):
            if mot.lower() in taches[i].lower():
                print(taches[i])
                trouve=True
        if trouve==False:
            print("Aucune tache trouvee.")
if ch==0:
    print("Programme fermer")