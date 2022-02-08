#Rayold Rakotonomenjanahary
#Numéro: 8884585
#Question2: Ce logiciel est utilisé pour afficher les entiers de a à b, incluant a et b entrés par l'utilsateur

a= int(input("SVP donner la valeur de a: "))
b= int(input("SVP donner la valeur de b: "))

#si "a" est inférieur à "b" alors on utilise cette condition
if (a<b):
    for compteur in range (a, b+1):
        print(compteur)

#si "a" est supérieur à "b" alors on utilise cette condition
elif(a>b):
    for compteur in range(a, b-1, -1):
        print(compteur)
        
