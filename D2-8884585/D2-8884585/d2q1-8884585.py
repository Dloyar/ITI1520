#Rayold Rakotonomenjanahary
#Numéro: 8884585
#Question1: Ce logiciel est utilisé pour calculer l'IMC qui indique le rapport entre le poids d’un adulte et la taille en mètres, au carré 

poids= float(input("SVP entrer votre poids en kilogrammes: "))
taille= float(input("SVP entrer votre taille en mètres: "))

def calculIMC(p, t):#cette fonction prend 2 arguments: p(poids) et t(Taille)
    "Fonction pour calculer l'IMC"
    IMC=(p/(t**2)) #le rapport entre le poids d’un adulte et la taille en mètres, au carré
    print("Votre IMC est ", IMC)
    #affiche à l'écran si le patient est maigre, normal, en surpoids ou obése
    if IMC < 18.5:
        print("Maigreur")
    elif IMC >=18.5 and IMC < 25:
        print("Poids idéal")
    elif IMC >= 25 and IMC < 30:
        print("Surpoids")
    elif IMC >= 30:
        print("Obésité")

calculIMC(poids, taille)#appel la fonction calcul de l'IMC
    
