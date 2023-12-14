class Routeur():
  def __init__(self, nom):
    # à compléter


  def maj_table(self, destination,passerelle,saut):
    # à compléter


  def recoit(self, routeur):
    # à compléter
    #on parcourt la table du routeur

        #ce n'est pas un lien vers ce routeur


            if
                # le routeur n'est pas dans la table : on l'ajoute


            else :
                # le routeur est déja dans la table : on met à jour la table





  def __str__(self):
    #ne pas modifier
    txt= self.nom+"\n"
    txt+="Routeur\tPasserelle\tDistance\n"
    for cle in self.table:
        txt+=str(cle)+"\t\t"+str(self.table[cle][0])+"\t\t\t"+str(self.table[cle][1])+"\n"
    return txt

