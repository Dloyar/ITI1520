#Rayold Rakotonomenjanahary
#Numéro: 8884585
#Question3: Ce logiciel permet à l'utilisateur de choisir un exercice entre l'addition et la multiplication

import random

def hasard():
    "fonction qui génére les nombres au hasard entre 1 à 9"
    nombre_hasard = random.randint(1,9)
    return nombre_hasard 

def exercice(opération):
    "fonction qui génére l'exercice d'addition ou multiplication selon le choix de l'utilisateur"
    print("SVP donner les réponses aux additions suivantes: ")
    compteur=1
    réponse_incorrect=0#variable pour stocker le nombre de réponse correcte
    #on utilise cette condition si l'opération est une addition
    if(opération == 0):
        while compteur <= 10:
            a=hasard()#génére les nombres au hasard entre 1 à 9
            b=hasard()#génére les nombres au hasard entre 1 à 9
            somme=a+b
            print(a,"+",b,"=", end=" ")
            réponse=int(input(""))
            if (réponse != somme):#donne la bonne réponse si la réponse donnée par l'utilisateur est fausse
                print("Incorrect - la réponse est ", somme)
                réponse_incorrect=réponse_incorrect+1#compte le nombre de réponse incorrecte 
            compteur = compteur+1
    #on utilise cette condition si l'opération est une multiplication
    elif(opération == 1):
        while(compteur <= 10):
            a=hasard()#génére les nombres au hasard entre 1 à 9
            b=hasard()#génére les nombres au hasard entre 1 à 9
            produit=a*b
            print(a,"*",b,"=", end=" ")
            réponse=int(input(""))
            if (réponse != produit):#donne la bonne réponse si la réponse donnée par l'utilisateur est fausse
                print("Incorrect - la réponse est ", produit)
                réponse_incorrect=réponse_incorrect+1#compte le nombre de réponse incorrecte 
            compteur = compteur+1

    réponse_correcte=10-réponse_incorrect#calcul le nombre de réponses correctes
    print(réponse_correcte, " réponses correctes.")
    if réponse_correcte > 6:#affiche le message « Félicitations! » si plus de 6 bonnes réponses ont été données
        print("Félicitations")
    else:#sinon il affiche le message « Demandez à votre enseignant(e)de vous aider. ».
        print("Demandez à votre enseignant(e) de vous aider.")
    
print("Ce logiciel va effectuer un test avec 10 questions...")
choix_opération= int(input("SVP choisissez l'opération 0)Addition 1)Multiplication(0 ou 1): "))#demande le choix d'opération à l'utilisateur
exercice(choix_opération)#appel la fonction exercice pour exécuter le logiciel

    
