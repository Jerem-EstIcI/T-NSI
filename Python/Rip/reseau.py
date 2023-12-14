from graph import Graphe

from routeur import Routeur


class Reseau():
    def __init__(self,schema):
        self.routeurs=Graphe()
        self.cablage(schema)

    def cablage(self,dico):
        '''construit un réseau en lui passant un graphe implémenté par un dictionnaire'''
        #création des noeuds (routeur)
        for cle in dico.keys():
            self.routeurs.ajouter_noeud(Routeur(cle))
        #création des connexions physiques
        for cle in dico.keys():
            noeud1=[i for i in  self.routeurs.liste_noeuds() if i.name==cle]
            for valeur in dico[cle]:
                noeud2=[i for i in self.routeurs.liste_noeuds() if i.name==valeur]
                self.routeurs.ajouter_arete(noeud1[0],noeud2[0])
        # initialisation des tables en fonction des connxions physiques
        for routeur in self.routeurs.liste_noeuds():
            for voisin in self.routeurs.voisins(routeur):
                routeur.maj_table(voisin.name,'_',1)


    def liste_routeurs(self):
        return self.routeurs.liste_noeuds()

    def voisins(self,routeur):
        return self.routeurs.voisins(routeur)


    def affiche(self):
        for routeur in self.routeurs.liste_noeuds():
            print(routeur)

