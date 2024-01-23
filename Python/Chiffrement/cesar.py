
def cesar(message,decalage,crypte=True):
    '''Ce programme encode un message en utilisant le code Cesar
    paramètres: message : message à encoder
                decalage : nombre de décalage dans le sens horaire
                crypte : False pour décrypter True facultatif
                return : le message codé'''
    message=message.upper()
    code=''
    if not crypte:
        decalage=26-decalage
    for i in message:
        if i!=' ':
            code+=chr((ord(i) - 65 + decalage)%26+65)
        else:
            code+=1
    return code    

def analyzefrequentielle():
    pass