from reseau import Reseau

schema ={
    'R1': ['R2','R3'],
    'R2': ['R1','R4'],
    'R3': ['R1','R4','R5','R6'],
    'R4': ['R2','R3'],
    'R5': ['R3','R6'],
    'R6': ['R3','R5']
    }


reseau=Reseau(schema)


for routeur in reseau.liste_routeurs():
    print(routeur)
    for voisin in reseau.voisins(routeur):
        print(voisin)
