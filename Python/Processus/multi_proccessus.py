# importation multiprocessing
import multiprocessing as mp
import os #pour afficher les pid et les ppid

#fonction à démarrer dans chaque  processus
def print_func(continent):
    a=0
	#on compte de 0 à 999999 --- changer éventuellement la valeur selon la rapidité de votre processeur---
    for i in range(1000000000):
        a+=1
		#la valeur n'est écrite que pour les multiple de 200000
        if a%200000==0:
            print( "ppid:\t", os.getppid(),"\tpid\t",os.getpid(),"\t",a,"\t",continent)

#le code est dans le programme principal
if __name__ == "__main__": 
	#combien de coeur dans le processeur
    nbcoeur= mp.cpu_count()
    print("Nombre de coeurs du cpu : ", nbcoeur)
	
    nbprocessus=7
    noms = ['Afrique','Asie','Antarctique','Europe','Amerique du Nord', 'Amérique du Sud', 'Océanie']
    #on restreint le nombre de processus :
    noms=noms[0:nbprocessus]
    procs = []
   
    # instanciation des processus avec arguments
    for nom in noms:
        #intialisation
        proc = mp.Process(target=print_func, args=(nom,))
        #mémorisation du processus
        procs.append(proc)
      
    #démarrage des processus
    for proc in procs:
        proc.start()
        print(proc)
       
    # terminaison des processus pour ne pas créer de zombies
    for proc in procs:
        proc.join()
        print(proc)