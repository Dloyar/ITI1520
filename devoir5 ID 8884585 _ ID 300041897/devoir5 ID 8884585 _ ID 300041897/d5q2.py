def etoiles(n):
  if (n != 0): 
    # On affiche une ligne de n étoiles
    for i in range(n):
      print('*', end='')
    print( )
    # On affiche le diagramme plus petit
    etoiles(n - 1)
    for i in range(n):
      print('*', end='')
    print( )       


   
def sommeListePos_rec(l, n):
  if (n == 0): 
      s = 0
  else:
      if l[n-1] > 0:
        s = sommeListePos_rec(l, n-1) + l[n-1]
      else:
        s = sommeListePos_rec(l, n-1)
        
  return s   

