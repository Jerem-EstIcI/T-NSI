class Routeur():
  def __init__(self, nom):
    # à compléter
    self.nom=nom
    self.table=dict() # ou {}

  def maj_table(self, destination,passerelle,saut):
    self.table[destination]=[passerelle,saut]

  def recoit(self, routeurVoisin):
    #on parcourt la table du routeur
    for cle in routeurVoisin.table.keys():
      if cle!=self.nom: #ce n'est pas un lien vers ce routeur   
        if not cle in self.table.keys(): # le routeur n'est pas dans la table : on l'ajoute
          self.maj_table(cle,routeurVoisin.nom,routeurVoisin.table(cle)[1]+1)
        else: # le routeur est déja dans la table : on met à jour la table
          AncienSaut=self.table[cle][1]
          if routeurVoisin.table(cle)[1]+1<AncienSaut:
            self.maj_table(cle,routeurVoisin.nom,routeurVoisin.table(cle)[1]+1)


  def __str__(self):
    #ne pas modifier
    txt= self.nom+"\n"
    txt+="Routeur\tPasserelle\tDistance\n"
    for cle in self.table:
        txt+=str(cle)+"\t\t"+str(self.table[cle][0])+"\t\t\t"+str(self.table[cle][1])+"\n"
    return txt

