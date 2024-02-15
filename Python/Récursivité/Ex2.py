#import de la librairie turtle
from turtle import *

def saucisson (n,d):
	#condtion d'arrêt : le niveau 1
    if n==1:
        forward (d) #on avance de la distance d
    else:
		#la largeur d'un segment s'obtient en divisant en 4 le segment d'origine
		#et on baisse le niveau de 1 pour tracer chaque morceau précédent
        d4=d/4
        n1=n-1
        saucisson(n1,d4) #appel récursif
        right (90) #on tourne à droite de 90°
        saucisson(n1,d4) #appel récursif
        left(90)#on tourne à gauche de 90°
        saucisson(n1,d4) #appel récursif
        left(90)#on tourne à gauche de 90°
        saucisson(n1,d4) #appel récursif
        saucisson(n1,d4) #appel récursif
        right(90) #on tourne à droite de 90°
        saucisson(n1,d4) #appel récursif
        right(90) #on tourne à droite de 90°
        saucisson(n1,d4) #appel récursif
        left(90)#on tourne à gauche de 90°
        saucisson(n1,d4) #appel récursif

def dessin ():  
    speed("fastest") # vitesse de déplacement de la tortue
    reset() # effacement du dessin précédent
    saucisson (3,100)

dessin()