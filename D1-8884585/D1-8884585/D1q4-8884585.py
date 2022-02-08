#Auteur: Rayold Rakotonomenjanahary
#Numéro:8884585
#quetion4
#Description du programme: Calcul le nombre de pièces minimum en
#utilisant une fonction

dollar=float(input("Entrez le montant en dollars: "))

def nombre_de_pièce(montant):
    quarter= int((montant*100)//25)
    dime= int(((montant*100)-(25*quarter))//10)
    nickel=int(((montant*100)-(25*quarter)-(10*dime))//5)
    pennie=int((montant*100)-(25*quarter)-(10*dime)-(5*nickel))
    pièce_min= quarter+dime+nickel+pennie
    return pièce_min

nbre_pièceMin = nombre_de_pièce(dollar)
print("Le nombre minimal de pièces que le caissier peut rendre est:",
      nbre_pièceMin)
