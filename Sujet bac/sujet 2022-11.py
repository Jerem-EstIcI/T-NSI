ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    '''
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
    '''
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = (position_alphabet(lettre) + decalage)%26
            resultat += ALPHABET[indice]
        else:
            resultat += lettre
    return resultat

cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4)
cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5)

