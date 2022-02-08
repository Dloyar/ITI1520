#Nom et Prénom: Rakotonomenjanahary Rayold  /ID:8884585
#Nom et Prénom:Abshir Amen /ID:300035421
#Devoir 4/ question1: créer 2 fonctions qui ajoutent 1 à chaque élément de la matrice
#dont l'une des fonction retourne rien et l'autre retourne une matrice
def ajoute(L):
    ''' (matrice) ->  none
    *prend une matrice et qui modifie la matrice en ajoutant 1 à tous les éléments
    '''
    #parcours tous les éléments de la matrice
    i = 0
    while i < len(L):
        j = 0
        while j<len(L[i]):
            L[i][j]= L[i][j]+1#ajoute 1 à chaque élément
            j = j + 1
        i = i + 1

def création_matrice():
    '''(none) ->  matrice
    *fonction qui génére une matrice
    '''
    m = int(input("Entrer le nombre de rangees: "))
    matrice = []#initialiser la matrice
    i = 0
    print("""Entrer les éléments de la matrice avec espaces entre les colonnes.
Une rangée par ligne, et une ligne vide à la fin.""")
    while i<m:
        rangee = [int(val) for val in input().split()]#entrer les éléments d'une ligne de la matrice
        matrice.append(rangee)#ajouté la rangé d'éléments dans la matrice
        i = i + 1
    return matrice

def ajoute_V2(l):
    '''(matrice) ->  matrice
    *fonction qui génére une matrice
    '''
    i = 0
    a = []#une nouvelle matrice pour tenir les valeurs des nouveaux éléments
    while i < len(l):
        j = 0
        a.append([])#création d'une rangée
        while j<len(l[i]):
            s= l[i][j]+1#ajout de 1 à chaque élément de la matrice
            a[i].append(s)#assigner les nouvelles valeurs dans la nouvelle matrice
            j = j + 1
        i = i + 1
    return a

#programme  principal
l=création_matrice()
print("\nla matrice est:")
print(l)#affiche la matrice originale
print("Apres exécution de la fonction ajoute, la matrice est:")
ajoute(l)#modifie la matrice originale en ajoutant 1 à chaque élément
print(l)#affiche la amtrice originale modifiée
print("Une nouvelle matrice créée avec ajoute_V2:")
print(ajoute_V2(l))#affiche la matrice modifiée et générée par la fonction ajoute_V2   
print("Apres exécution de la fonction ajoute_V2, la matrice initiale est:")
print(l)#matrice i initiale
