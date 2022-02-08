#Rayold Rakotonomenjanahary
#Numéro: 8884585
#Question4: Ce logiciel teste l’élève avec 10questions qui sont distribuées de manière aléatoire entre multiplication et addition.

import random

def hasard():
    "fonction qui génére les nombres au hasard entre 1 à 9"
    nombre_hasard = random.randint(1,9)
    return nombre_hasard 


def exercice():
    "fonction qui génére aléatoirement un exercice d'addition ou multiplication"
    compteur = 1
    réponse_incorrect = 0
    while(compteur <= 10):
        opération = random.randint(0,1)#elle génère alors deux nombres aléatoires pour la question(1 pour multiplication ou 0 pour addition)
        if(opération == 0):#addition
            a=hasard()#génére les nombres au hasard entre 1 à 9
            b=hasard()#génére les nombres au hasard entre 1 à 9
            somme=a+b
            print(a,"+",b,"=", end=" ")
            réponse=int(input(""))
            if (réponse != somme):#donne la bonne réponse si la réponse donnée par l'utilisateur est fausse
                print("Incorrect - la réponse est ", somme)
                réponse_incorrect=réponse_incorrect+1
        
        elif(opération == 1):#multiplication
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
    if réponse_correcte > 6:
        print("Félicitations")
    else:
        print("Demandez à votre enseignant de vous aider.")

print("Ce logiciel va effectuer un test avec 10 questions...")
exercice()#appel la fonction exercice pour exécuter le logiciel


    
