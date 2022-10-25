from calendar import MONDAY
import random

# 1. cette partie choisi un mot aléatoire
mots = [] 
with open ("dico_france.txt") as read_file: 
    for line in read_file: 
        mots.append(line.rstrip("\n")) 
mot = random.choice(mots) 



# déclaration des variables
lettres = [] 
faux = 0 
trouvé = False 

# choix de niveau

niveau=[]

while niveau != 1 and niveau != 2 and niveau != 3:
    niveau = int(input ("Bienvenu dans le jeu de pendu!\nChoisissez un niveau :\n1 = Debutant / 2 = Intermediaire / 3 = Expert\n-->"))

    if niveau == 1:
        vies = 10
    elif niveau == 2:
        vies = 7
    elif niveau == 3:
        vies = 4
    else:
        print("Erreur, veuillez choisir un niveau entre 1 et 3.")


# Le programme avec les boucles et les conditions
while not trouvé: 
    trouvé = True 
    
    nb_vies_depart = vies
    
    vies_restantes = nb_vies_depart - faux
 

    # la partie qui affiche les "_" au lieu des lettres
    for la_lettre in mot: 
        if la_lettre in lettres:
            print(la_lettre, end=" ")
        else: #sinon
            trouvé = False 
            print("_", end=" ")

    

      # programme pour afficher les vies restantes
    print() 
    print("Nombre de vie(s) restante(s) : " , vies_restantes)
    
    
    # Fonction pour afficher les lettres utilisées
    print("Lettres proposées : ", end="")  

    for la_lettre in lettres: 
        print(la_lettre, end=" | ") 
        
    

    # fonction de limite de nombres de vies et d'affichage de message perdu puis arret de la programme
    if faux >= nb_vies_depart: 
        print()
        
        print("Perdu !") 
        print("Le mot était : {}".format(mot))
        break 
    
    # fonction pour afficher la victoire en cas d'avoir trouver toutes les lettres , puis arret de la programme
    if trouvé: 
        print()
        print("Tu as gagné!")
        break 
    
    # fonction d'input
    print() 
    
    lettre = input("Quelle lettre proposes tu ? : ") 
    print()
    if lettre in mot:
        print("################# BRAVO ! Tu vins de trouver une lettre #################")
        print()

    
    
    #function de rédirection d'input dans lettres pour ensuite vérifier si la lettre se trouve dans cette liste des lettres
    lettres.append(lettre) 

    if lettre not in mot: #
        faux += 1 
    

    

