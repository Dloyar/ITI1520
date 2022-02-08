#Auteur: Rayold Rakotonomenjanahary
#8884585
#Quetion2
#Description du programme: Calcul le nombre de pièce minimal 

montant=float(input("Entrez le montant en dollars: "))

quarter= int((montant*100)//25)
dime= int(((montant*100)-(25*quarter))//10)
nickel=int(((montant*100)-(25*quarter)-(10*dime))//5)
pennie=int((montant*100)-(25*quarter)-(10*dime)-(5*nickel))

print("Le nombre minimal de pièces que le caissier peut rendre est:",
      quarter+dime+nickel+pennie)
