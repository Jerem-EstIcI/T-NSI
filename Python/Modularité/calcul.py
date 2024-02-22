def TSD(a,b,c):
    '''résout un TSD d'équation a*x²+b*x+c=0
    paramètres : a,b et c les coéfficients nombres entiers
    return [solution1,solution2] ou None si pas de solutions
    '''
    delta=b*b-4*a*c
    if delta<0:
        return None
    else:
        return [(-b-delta**0.5/2*a),(-b+delta**0.5/2*a)]
    
def ProduitVectoriel(ax,ay,az,bx,by,bz):
    '''résout une équation vectoriel en renvoyant l'ensemble des réponses
    paramètres : ax,ay,az,bx,by,bz
    return [solution1,solution2,solution3]
    '''
    return [(ay*bz-az*by),(az*bx-ax*bz),(ax*by-ay*bx)]
