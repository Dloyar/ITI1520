#Nom et Prénom: Rakotonomenjanahary Rayold  /ID:8884585
#Nom et Prénom:Abshir Amen /ID:300035421
#Devoir 4/ question1:classe du fichier d4q2.py qui contient les fonctions:
#*effaceTableau(Tab)
#*verifieGagner(tab)
#*testLignes(tab)
#*testCols(tab)
#*testDiags(tab)
#*testMatchNul(tab)
def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
    # a completer
   #cette fonction parcours tous les éléments
   #de la matrice et les réanitialise en "-"
   i=0
   while i < len(tab):
      j = 0
      while j < len(tab[i]):
         tab[i][j] = "-"#réanitialise en "-"
         j = j + 1
      i = i + 1
    # retourne rien

      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer
    if testLignes(tab) != "-":#vérifie si une ligne est gagnante
       print("Joueur",testLignes(tab),"a gagné!")
       return True
    elif testCols(tab) != "-":#vérifie si une colonne est gagnante
       print("Joueur",testCols(tab),"a gagné!")
       return True
    elif testDiags(tab) != "-":#vérifie si une diagonle est gagnante
       print("Joueur",testDiags(tab),"a gagné!")
       return True
    elif testMatchNul(tab):#vérifie s'il y a match nul 
       print("Match nul")
       return True
      
    return False  # a changer

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   i = 0
   while i < len(tab):
      j = 0
      x = 0#valeur pour compter le nombre de "X" dans une ligne  
      O = 0#valeur pour compter le nombre de "O" dans une ligne
      while j<len(tab):
         if tab[i][j] == "X":
            x = x +1#compte le nombre de "X"
         elif tab[i][j] == "O":
            O = O + 1#compte le nombre de "O"
         j = j + 1
      if x == 3:
         return "X"
         break
      elif O == 3:
         return "O"
         break
      i = i + 1
   return '-' # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   i = 0
   while i < len(tab):
      j = 0
      x = 0#valeur pour compter le nombre de "X" dans une colonne
      O = 0#valeur pour compter le nombre de "O" dans une colonne
      while j<len(tab):
         if tab[j][i] == "X":
            x = x+1#incrémenter x si l'élément de tab est égal à "X" 
         elif tab[j][i] == "O":
            O = O+1#incrémenter O si l'élément de tab est égal à "O"
         j = j + 1
      if x == 3:#si x = 3 alors la fonction s'arrête immédiatement et retourne "X"
         return "X"
         break
      elif O == 3:#si O = 3 alors la fonction s'arrête immédiatement et retourne "O"
         return "O"
         break
      i = i + 1
  
   return '-'   #a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   #vérification de la première diagonale
   i = 0
   x = 0#valeur pour compter le nombre de "X" dans une diagonale
   O = 0#valeur pour compter le nombre de "O" dans une diagonale
   while i<len(tab):
      if tab[i][i] == "X":
         x= x + 1
      elif tab[i][i] == "O":
         O = O + 1
      i = i + 1
      if x == 3:
         return "X"
         break
      elif O == 3:
         return "O"
         break

   #vérification de la deuxième diagonale
   if tab[2][0]== "X" and tab[2][0]== tab[1][1] and  tab[2][0] == tab[0][2]: 
      return "X"
   elif tab[2][0]=="O" and tab[2][0]== tab[1][1] and  tab[2][0] == tab[0][2]: 
      return "O"

   
    
   return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   i=0
   while i < len(tab):
      j = 0
      while j < len(tab[i]):
         if tab[i][j] == "-":#si un élément de la liste est égal "-" alors la foction retourne true ets'arrête immédiatement
            return False
            break
         j = j + 1
      i = i + 1
  
   return True  # a changer

