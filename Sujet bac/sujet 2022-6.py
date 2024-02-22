def maxi(tab):
    '''
    >>>maxi([1,5,6,9,1,2,3,7,9,8])
    (9,3)
    '''
    maxc=tab[0]
    maxi=0
    for i in range(len(tab)):
        if tab[i]>maxc:
            maxc=tab[i]
            maxi=i
    return (maxc,maxi)

def rechercheindice(gene,seq_adn):
    '''
    rechercheindice("AATC","GTACAAATCTTGCC")
    True
    rechercheindice("AGTC","GTACAAATCTTGCC")
    False
    '''
    n=len(seq_adn)
    g=len(gene)
    i=0
    indice=-1
    while i<n:
        j=0
        while j<g and gene[j] == seq_adn[i+j]:
            j+=1
        if j == g:
            indice=i
        i+=1
    return indice

def recherche(gene,seq_adn):
    '''
    recherche("AATC","GTACAAATCTTGCC")
    True
    recherche("AGTC","GTACAAATCTTGCC")
    False
    '''
    n=len(seq_adn)
    g=len(gene)
    i=0
    solution=False
    while i<n:
        j=0
        while j<g and gene[j] == seq_adn[i+j] and solution==False:
            j+=1
        if j == g:
            solution=True
        i+=1
    return solution
