# fonctions auxiliaires pour visualiser  une grille 
def affiche(g):
    for l in g:
        for x in l:
            print(x, sep="", end=" ")
                           
        print()

# la fonction de propagation: ici on modifie la grille au fur et à  mesure
# ainsi on n'a pas besoin de mémoriser si la case a été visitée
def propagation(g,i,j, val):
    # A COMPLETER
	# Condition d'arrêt
    if g[i][j] == val:
        g[i][j]=0
        if i<len(g)-1:
            propagation(g,i+1,j,val)  
        if i>0:
            propagation(g,i-1,j,val)  
        if j<len(g)-1:
            propagation(g,i,j+1,val)  
        if j>0:
            propagation(g,i,j-1,val)
    else:
        return None
	   
	#corps de la fonction récursive
	   
	   
	   
#test sur l'exemple
grille=[
	[2,2,4,2,2,2,1],
	[1,4,1,1,2,3,1],
	[4,2,4,1,4,2,4],
	[4,2,4,2,4,4,4],
	[4,3,4,1,4,3,3],
	[1,1,3,3,3,1,2],
	[4,4,2,2,3,3,1]
]

def test(g,i,j):
	#on récupère la valeur dans la case(i,j) de la grille
    valeur=g[i][j]
    #on exécute la fonction récursive de propagation 
    propagation(g,i,j,valeur)
    #on affiche le résultat
    affiche(g)
#lancement du test	
test(grille,3,4)
print("----------------------")
test(grille,5,3)