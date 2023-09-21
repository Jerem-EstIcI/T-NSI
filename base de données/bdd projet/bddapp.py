import tkinter as tk
from tkinter import ttk
import sqlite3
import os.path

#----------------------------------------------------------------------------------

bddApp = tk.Tk()
bddApp.title("Base de données")
IconPath = os.path.abspath("icon.ico")
bddApp.iconbitmap(IconPath)
bddApp.resizable(False,False)

#----------------------------------------------------------------------------------

def peuple_realisateur():
    '''
    méthode qui remplit la comboBox combo_realisateur
    paramètre : aucun
    retour : liste des réalisateurs contenus dans la base 'box_office.db'
    '''
    maBase=sqlite3.connect('box_office.db')
    curseur=maBase.cursor()
    curseur.execute('''SELECT nom,prenom FROM realisateur ORDER BY nom''')
    liste=curseur.fetchall()
    maBase.close()
    #mise en forme des réalisateurs avec nom et prénom :
    #ce n'est pas un espace mais alt+255
    liste_realisateur=[]
    for rea in liste:
       liste_realisateur.append(rea[0]+" "+rea[1])
    return liste_realisateur

combo_realisateur = ttk.Combobox(bddApp,values=peuple_realisateur())
combo_realisateur.grid(row=0, column=0)

#----------------------------------------------------------------------------------

def afficher_film_realisateur(event):
    # Obtenir le réalisateur sélectionné à partir de combo_realisateur
    selected_realisateur = combo_realisateur.get()
    # Diviser selected_realisateur en nom et prénom
    nom, prenom = selected_realisateur.split()
    
    maBase = sqlite3.connect('box_office.db')
    curseur = maBase.cursor()
    
    # Fournir les valeurs pour les espaces réservés (?, ?)
    curseur.execute('''SELECT titre FROM film 
                    JOIN est_realise_par ON est_realise_par.id_film = film.id_film
                    JOIN realisateur ON est_realise_par.id_rea = realisateur.id_rea
                    WHERE nom=? AND prenom=?''', (nom, prenom))
    
    # Récupérer les résultats et fermer la connexion à la base de données
    liste = curseur.fetchall()
    maBase.close()
    
    # Extraire les titres des films à partir des résultats de la requête
    liste_film = [film[0] for film in liste]
    
    # Effacer et mettre à jour la liste des titres de films dans la listeBox
    listeFilm.delete(0, tk.END)
    for titre_film in liste_film:
        listeFilm.insert(tk.END, titre_film)

#----------------------------------------------------------------------------------

def afficher_entree_film(event):
    selected_realisateur = combo_realisateur.get()
    nom, prenom = selected_realisateur.split()

    maBase = sqlite3.connect('box_office.db')
    curseur = maBase.cursor()
    curseur.execute('''SELECT film.entree FROM film 
                    JOIN est_realise_par ON est_realise_par.id_film = film.id_film
                    JOIN realisateur ON est_realise_par.id_rea = realisateur.id_rea
                    WHERE realisateur.nom=? AND realisateur.prenom=?''', (nom, prenom))

    liste_entrees = curseur.fetchall()
    maBase.close()

    listeEntrees.delete(0, tk.END)
    for entree in liste_entrees:
        listeEntrees.insert(tk.END, entree)

#----------------------------------------------------------------------------------

def afficher_annee_film(event):
    selected_realisateur = combo_realisateur.get()
    nom, prenom = selected_realisateur.split()

    maBase = sqlite3.connect('box_office.db')
    curseur = maBase.cursor()
    curseur.execute('''SELECT film.annee FROM film 
                    JOIN est_realise_par ON est_realise_par.id_film = film.id_film
                    JOIN realisateur ON est_realise_par.id_rea = realisateur.id_rea
                    WHERE realisateur.nom=? AND realisateur.prenom=?''', (nom, prenom))

    liste_Annee = curseur.fetchall()
    maBase.close()

    listeAnnee.delete(0, tk.END)
    for annee in liste_Annee:
        listeAnnee.insert(tk.END, annee)

#----------------------------------------------------------------------------------
def afficher_nation_film(event):
    selected_realisateur = combo_realisateur.get()
    nom, prenom = selected_realisateur.split()

    maBase = sqlite3.connect('box_office.db')
    curseur = maBase.cursor()
    
    # Retrieve nationality information for movies associated with the director
    curseur.execute('''SELECT film.titre, GROUP_CONCAT(nationalite.nation, '/') FROM film
                    JOIN est_de_nationalite ON film.id_film = est_de_nationalite.id_film
                    JOIN est_realise_par ON est_de_nationalite.id_film = est_realise_par.id_film
                    JOIN realisateur ON est_realise_par.id_rea = realisateur.id_rea
                    JOIN nationalite ON est_de_nationalite.id_nation = nationalite.id_nation
                    WHERE realisateur.nom=? AND realisateur.prenom=?
                    GROUP BY film.titre''', (nom, prenom))

    liste_Nation = curseur.fetchall()
    maBase.close()

    listeNation.delete(0, tk.END)
    for film, nationalites in liste_Nation:
        listeNation.insert(tk.END, nationalites)


#----------------------------------------------------------------------------------

liste=tk.Variable(bddApp,['']) #la variable associée aux éléments de la liste
#--
listeFilm=tk.Listbox(bddApp,listvariable=liste)
listeFilm.grid(row=1, column=0)
#--
listeEntrees = tk.Listbox(bddApp)
listeEntrees.grid(row=1, column=1)
#--
listeAnnee = tk.Listbox(bddApp)
listeAnnee.grid(row=1, column=2)
#--
listeNation = tk.Listbox(bddApp)
listeNation.grid(row=1, column=3)

#----------------------------------------------------------------------------------

def update_display(event):
    afficher_film_realisateur(event)
    afficher_entree_film(event)
    afficher_annee_film(event)
    afficher_nation_film(event)

# mise en place de l'écouteur sur la comboBox (to bind = lier)
# A chaque fois qu'on sélectionne un autre item de la comboBox, la méthode afficher_film_realisateur est appelée
combo_realisateur.bind("<<ComboboxSelected>>", update_display)


bddApp.mainloop()