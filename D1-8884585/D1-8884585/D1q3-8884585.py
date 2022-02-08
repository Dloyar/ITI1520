#Auteur: Rayold Rakotonomenjanahary
#8884585
#question3
#Description du programme: Convertie le résultat de livre et once en kg en
#utilisant une fonction

livre = int(input("Entrez le nombre de livres: "))
once = float(input("Entrez le nombre d'onces: "))

def conversion_once_livre(a,b):
    kg = a*0.4536 + b*0.0283
    return kg

kg=conversion_once_livre(livre,once)
print(livre, "livre et", once, "équivalent à ", kg, "kilogrammes")

