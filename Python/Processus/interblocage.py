import threading
from time import sleep

#fonction d'intelligence artificielle
#qui décide si la voiture avance
def avance(numero):
    print("La voiture ",  couleurAutos[numero], "est sur le carrefour")
    #délai pour attendre que les threads soient tous démarrés
    sleep(nbVoitures)
    #identification du numéro du véhicules à droite
    numeroDroite=(numero+1) % nbVoitures
    #tant que la place de carrefour n'est pas libérée, la voiture n'a pas avancé
    while occupations[numero] :
		#affichage de tous les threads et le numéro du thread en cours 
		#(la ligne suivante est à décommenter pour observer l'état des threads)
        print(voitures,threading.get_ident())
        sleep(0.1)
        #elle ala priorité : elle ne bouge pas 
        if  priorites[numeroDroite]:
            print('La voiture ', couleurAutos[numero] ,' attend que la voiture ', couleurAutos[numeroDroite],' soit passée')
            # jusqu'à le thread de la voiture de droite soit terminé ?
            voitures[numeroDroite].join()
        #sinon elle avance    
        else:
            print("La voiture ", couleurAutos[numero], " roule et libère le carrefour")
            #elle libère sa place
            occupations[numero]=False
            #elle perd donc sa priorité par rapport au véhicule qui était à sa gauche
            priorites[numero]=False

#nombre de voitures (max 9 sinon ajouter des couleurs)
nbVoitures = 9
#couleurs des voitures
couleurAutos=['bleue','jaune','rouge','verte','noire','blanche','marron','orange','violette']
#toutes les places sont occupées
occupations=[True for i in range(nbVoitures)]
#toutes les voitures bénéficie de la priorité à droite
priorites=[True for i in range(nbVoitures)]
#on supprime la priorité de la voiture bleue en décommentant la ligne ci-dessous
priorites[0]=False
#on crée autant de thread que de voitures : les IA sont initialisées
voitures = [threading.Thread(target=avance,   args=(numero,))  for numero in range(nbVoitures)]
#(la ligne suivante est à décommenter pour observer l'état des threads)
print(voitures,threading.get_ident())
#démarrage des IA
for voiture in voitures:
    voiture.start()
    sleep(0.5)
print("Les voitures autonomes sont toutes sur le carrefour. Que leurs IA se débrouillent....") 