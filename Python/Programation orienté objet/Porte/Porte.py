class Porte:
    '''
    Définit une porte
    paramètres :    x position horizontale  int
                     y position verticale    int
                     c couleur               string
    '''
    def __init__(self,x,y,c):
        self.x=x
        self.y=y
        self.couleur=c
        self.verrou=False
    def verrouiller(self): # la méthode ne nécessite aucun attribut
        self.verrou=not self.verrou
    def peindre(self,c): # la méthode nécessite un (ou plusieurs) attribut
        self.couleur=c


        
porte1=Porte(10,0,'brown')
print(porte1.couleur)
porte1.verrouiller()
print(porte1.verrou)
#porte1.peindre()
porte1.peindre('yellow')
print(porte1.couleur)