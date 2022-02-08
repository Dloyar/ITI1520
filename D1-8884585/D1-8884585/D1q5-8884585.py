#Auteur: Rayold Rakotonomenjanahary
#8884585
#Question5
#Description du programme:Converstie l'année lumière en seconde puis en km et
#enfin calcul la distance entre 2 étoiles

année_sidérale=int(input("Entrez un nombre d’années-lumière:"))

def convertir_en_seconde(année):
    seconde_sidérale = 365.26*86400
    seconde= année*seconde_sidérale
    return seconde

seconde_lumière = convertir_en_seconde(année_sidérale)
print("Le nombre de secondes-lumière est", seconde_lumière)

def convertir_en_kilomètre(seconde):
    km = seconde*300000
    return km

distance = convertir_en_kilomètre(seconde_lumière)
print("La distance est ", distance, "km")

étoile1=float(input("Entrez la distance de la première étoile, en années-lumière:"))
étoile2=float(input("Entrez la distance de la deuxième étoile, en années-lumière:"))

def distance_entre_2étoiles(lumière1,lumière2):
    y1=convertir_en_seconde(lumière1)
    x1=convertir_en_kilomètre(y1)
    y2=convertir_en_seconde(lumière2)
    x2=convertir_en_kilomètre(y2)
    écart= (x1+x2)
    return écart

distance_en_km=distance_entre_2étoiles(étoile1,étoile2)
print("La distance entre les deux étoiles est", distance_en_km, "km.")
