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
combo_realisateur.grid(row=0, column=1)

#----------------------------------------------------------------------------------

def afficher_film_realisateur(event):
    # Obtenir le réalisateur sélectionné à partir de combo_realisateur
    realisateur_selectionner = combo_realisateur.get()
    
    # Diviser realisateur_selectionner en nom et prénom en utilisant la première occurrence d'un espace comme séparateur
    parts = realisateur_selectionner.split(' ', 1)
    nom = parts[0] if len(parts) > 0 else ''
    prenom = parts[1] if len(parts) > 1 else ''

    maBase = sqlite3.connect('box_office.db')
    curseur = maBase.cursor()

    curseur.execute('''SELECT titre FROM film 
                    JOIN est_realise_par ON est_realise_par.id_film = film.id_film
                    JOIN realisateur ON est_realise_par.id_rea = realisateur.id_rea
                    WHERE nom=? AND prenom=?''', (nom, prenom))

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
    realisateur_selectionner = combo_realisateur.get()

    parts = realisateur_selectionner.split(' ', 1)
    nom = parts[0] if len(parts) > 0 else ''
    prenom = parts[1] if len(parts) > 1 else ''

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
    realisateur_selectionner = combo_realisateur.get()
   
    parts = realisateur_selectionner.split(' ', 1)
    nom = parts[0] if len(parts) > 0 else ''
    prenom = parts[1] if len(parts) > 1 else ''

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
    realisateur_selectionner = combo_realisateur.get()
    
    parts = realisateur_selectionner.split(' ', 1)
    nom = parts[0] if len(parts) > 0 else ''
    prenom = parts[1] if len(parts) > 1 else ''

    maBase = sqlite3.connect('box_office.db')
    curseur = maBase.cursor()
    
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
var_tri = tk.StringVar()

def trier():
    tri_par = var_tri.get()
    if tri_par == "titre":
        # ?
        pass
    elif tri_par == "entrees":
        # ?
        pass
    elif tri_par == "annees":
        # ?
        pass
    elif tri_par == "nations":
        # ?
        pass

def decroissant():
    # ?
    pass

#----------------------------------------------------------------------------------

label_films = tk.Label(bddApp, text="Titres")
label_films.grid(row=1, column=1)

label_entrees = tk.Label(bddApp, text="Entrées")
label_entrees.grid(row=1, column=2)

label_annees = tk.Label(bddApp, text="Années")
label_annees.grid(row=1, column=3)

label_nations = tk.Label(bddApp, text="Nation")
label_nations.grid(row=1, column=4)

#----------------------------------------------------------------------------------

liste=tk.Variable(bddApp,['']) #la variable associée aux éléments de la liste
#--
listeFilm=tk.Listbox(bddApp,listvariable=liste,width=40)
listeFilm.grid(row=2, column=1)
#--
listeEntrees = tk.Listbox(bddApp)
listeEntrees.grid(row=2, column=2)
#--
listeAnnee = tk.Listbox(bddApp)
listeAnnee.grid(row=2, column=3)
#--
listeNation = tk.Listbox(bddApp)
listeNation.grid(row=2, column=4)

#----------------------------------------------------------------------------------
label_films = tk.Label(bddApp, text="Trier par :")
label_films.grid(row=3, column=0)

bouton_tri_titre = ttk.Radiobutton(bddApp, text="Titre", variable=trier, value="titre")
bouton_tri_titre.grid(row=3, column=1)

bouton_tri_entrees = ttk.Radiobutton(bddApp, text="Entree", variable=trier, value="entrees")
bouton_tri_entrees.grid(row=3, column=2)

bouton_tri_annees = ttk.Radiobutton(bddApp, text="Année", variable=trier, value="annees")
bouton_tri_annees.grid(row=3, column=3)

bouton_tri_nation = ttk.Radiobutton(bddApp, text="Nation", variable=trier, value="nations")
bouton_tri_nation.grid(row=3, column=4)
()
bouton_decroissant = tk.BooleanVar()
bouton_decroissant = tk.Checkbutton(bddApp, text="Décroissant", variable=bouton_decroissant, command=decroissant)
bouton_decroissant.grid(row=3, column=5)

#----------------------------------------------------------------------------------

def affichage_table(event):
    afficher_film_realisateur(event)
    afficher_entree_film(event)
    afficher_annee_film(event)
    afficher_nation_film(event)

# mise en place de l'écouteur sur la comboBox (to bind = lier)
# A chaque fois qu'on sélectionne un autre item de la comboBox, la méthode afficher_film_realisateur est appelée
combo_realisateur.bind("<<ComboboxSelected>>", affichage_table)


bddApp.mainloop()