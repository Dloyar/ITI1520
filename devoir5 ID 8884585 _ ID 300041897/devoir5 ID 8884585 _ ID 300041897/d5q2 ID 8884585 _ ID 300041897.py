#Auteurs:_Rayold Rakotonomenjanahary ID:8884585
#        _Sydroy Rakotonomenjanahary ID:300041897
#devoir 5 question 2
#question a: Ecrire une fonction Python récursive appelée etoiles qui prendra comme paramètre un
#entier non négatif et qui générera un dessin composé d’étoiles
def etoiles(a):
    '''(int)->None
    imprime des étoiles'''
    if  a == 1:     #condition si a est égale à 1
        print("*")  #affiche le dessin d'un étoile à l'écran si a = 1
    else:
        print("*"*a)#affiche des étoiles dans l'ordre décroissant
        etoiles(a-1)#répéter la fonction
    print("*"*a)    #affiche des étoiles dans l'ordre croissant 

#programme principal    
etoiles(4)#appel de la fonction étoiles

    
#question b:
def sommeListePos_rec(l,n):
    '''(liste, int)->int
    calcul la somme des valeurs positives dans une liste'''
    if n == 1:#condition si n est egale a 1
        if l[0]>0: 
            s = l[0] #prend la valeur du chiffre à la 1ère position si il est positif, s est la variable pour stocker la somme
        else:
            s=0      #sinon la valeur de s est posé à 0
    else:
        sPartielle = sommeListePos_rec(l,n-1) #repete la fonction 
        s =sPartielle#donne la valeur de s
        if l[n - 1]> 0:   #on prend que les valeurs superieur a 0
            s = sPartielle + l[n-1] #on ajoute la valeur positif à la somme s
    return s

#programme principal
l = [1,-2,5,0,-5]
print("Somme: ",sommeListePos_rec(l, len(l)))#exécution de la fonction et affichage de la somme
    
