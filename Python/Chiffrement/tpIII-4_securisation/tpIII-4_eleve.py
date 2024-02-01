# Créé par LELOIRE, le 24/01/2024 en Python 3.7


# *****************   NE PAS MODIFIER ************************************

#création de l'ensemble des mots courant du français dans l'ensemble dico
with open("francais.txt", encoding="utf-8") as file:
   	dico = set(line.strip().upper() for line in file)



def indexMax(liste):
    '''fonction qui renvoie l'index du maximum d'une liste d'entier
    paramètre   : liste  liste d'entier
    retour      : index  du maximum
    Exemple indexMax([1,5,2,7,3] renvoie 3
    Si le maximun est présent plusieurs fois, renvoie le dernier index
    '''
    max=0
    index=0
    for i in range(len(liste)):
        if liste[i]>max:
            max=liste[i]
            index=i
    return index

#message codé clé de décalage inconnue
c='X GZ PQE BXGE SDMZPE PQRUE QF X GZQ PQE BXGE SDMZPQE DQMXUEMFUAZE P MXMZ FGDUZS MGDM QFQ PQ FDAGHQD GZQ YQFTAPQ PQ PQODKBFMSQ PG PUEBAEUFUR MXXQYMZP QZUSYM OQXGU OU MHMUF QFQ UZHQZFQ HUZSF MZE BXGE FAF BMD X UZSQZUQGD QXQOFDUOUQZ MXXQYMZP MDFTGD EOTQDNUGE P MBDQE GZ NDQHQF PQ X UZHQZFQGD ZQQDXMZPMUE TGSA WAOT PQBAEQ QZ WEWE M XM NMEQ PQBAEQQ OAYYQ YMOTUZQ OUHUXQ QXQOFDAYQOMZUCGQ BAGD ODKBFQD XQE YQEEMSQE OAYYQDOUMGJ QXXQ RAZOFUAZZMUF QZ QZFDMZF EGD GZ OXMHUQD EQYNXMNXQ M GZQ YMOTUZQ M QODUDQ PQE XQFFDQE PQ RMOAZ FAGF M RMUF OXMEEUCGQ GZQ FAGOTQ BQDYQFFMUF QZEGUFQ P QZHAKQD GZ OAGDMZF QXQOFDUCGQ BMDOAGDUD XQ OMNXMSQ PQ DAFADE GZQ EQDUQ PQ PUECGQE QZ YQFMX BQDYQFFMZF P QZOAPQD XQ YQEEMSQ QZ FDMZERADYMZF XM XQFFDQ UZUFUMXQ QZ GZQ ZAGHQXXQ XQFFDQ'




# *******************  A PROGRAMMER *****************************************

def code(m,d):
    '''fonction qui encode un message en utilisant le code Cesar
        paramètres : m : message à encoder sans accent
                     d : nombre de décalage dans le sens horaire
        return : le message codé
    '''
    #conversion en majuscule
    m=m.upper()
    c=''
    for l in m: # pour les lettres dans le message
        if l==' ':
            c+=' '
        else:
            asc=(ord(l)-65+d)%26+65 
            c+=chr(asc) # trasnforme en lettre
    return c

def decode(c,d):
    '''fonction qui décode un message en utilisant le code Cesar
        paramètres : c : message à décoder en majuscule non accentué
                     d : nombre de décalage dans le sens horaire
        return : le message en clair
    '''
    d=26-d
    m=code(c,d)
    return m


def brute1(c):
    '''fonction qui renvoie la liste des décodage avec les 25 décalages possibles
        paramètre : c message codé
        return : liste de 25 decodages'''
    liste=[]
    for d in range(25):
        liste.append(decode(c,d))
    return liste




def brute2(liste):
    '''fonction qui renvoie la liste des 25 décodages possibles
        paramètre : liste donnée par brute1
        return : le décodage le plus probable

        utilise dico pour tester les mots

    '''
    # nombre de mot du dico reconnu dans chaque décodage
    # 0 avant traitement
    score=[0 for i in range(26)]
    for i in range(0,len(liste)):
        for mot in liste[i].split():
            if mot in dico:
                score[i]+=1
    d=indexMax(score)
    print('le decalage est : ',d+1)
    # ligne ci-dessous à décommenter
    # return liste[d]



def frequentiel(c):
    '''
    fréquence qui utilise le fait que le E (5 ième lettre) est la lettre la plus fréquente en français
    paramètre : c le message codé
    return : le message décodé
    '''
    # met à 0 le tableau de fréquence des lettres trouvées
    frequence=[0 for i in range(26)]
    for l in c:
        if l!=' ':
            frequence[ord(l)-65]+=1
    print('freq',frequence)





    #calcul de d  (0 à remplacer par le bon code)
    d=indexMax(frequence)-4%26
    return decode(c,d)



# *******************   TESTE SUCCESSIVEMENT VOS FONCTIONS   *******************
# *******************         NE PAS MODIFIER                *******************

#question I1.a
print ("\nQuestion I1.a\n")
test1="essai"
codage = code(test1,7)
print(codage)
decodage=decode(codage,7)
print(decodage)



#question I.1.b
print ("\nQuestion I1.b\n")
liste = brute1(c)
for element in liste:
    print(element)
    print('\n Suivant \n')



#question I.1.c
print ("\nQuestion I1.c\n")
liste = brute1(c)
print(brute2(liste))



# question I.1.d
print ("\nQuestion I1.d\n")

print(frequentiel(c))







