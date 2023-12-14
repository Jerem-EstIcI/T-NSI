class Graphe():
    def __init__(self, noeuds = None):
        """Initialisation avec un graphe vide
        __noeuds est un dictionnaire
        - clé = Valeur du noeud (chaine, entier)
        - valeur = liste d'aretes (clé, poids)"""
        if noeuds is None:
            self.__noeuds = dict()
        else:
            self.__noeuds = noeuds

    def ajouter_noeud(self, nd):
        """Ajoute un nouveau noeud au graphe"""
        if not nd in self.__noeuds:
            self.__noeuds[nd] = []

    def ajouter_arete(self, nd1, nd2, poids=1):
        """Ajoute une arête au graphe
        si poids n'est pas renseigné, il prendra la valeur 1"""
        # On s'assure que les arètes existent
        self.ajouter_noeud(nd1)
        self.ajouter_noeud(nd2)
        # On crée la connexion nd1 -> nd2
        self.__noeuds[nd1].append((nd2, poids))

    def liste_noeuds(self):
        """Renvoie la liste des noeuds"""
        nds = list(self.__noeuds.keys())
        return nds

    def voisins(self, nd):
        """Renvoie la liste des noeuds voisins de nd"""
        if nd in self.liste_noeuds():
            return [a[0] for a in self.__noeuds[nd]]
        else:
            return []

    def arete(self,nd1, nd2):
        """Renvoie le poids de l'arete nd1->nd2 ou 0 si pas d'arête"""
        if nd2 not in self.voisins(nd1):
            return 0
        for a in self.__noeuds[nd1]:
            if a[0] == nd2:
                return a[1]



