def decode(message,cle):
    result=''
    #la cle a le meme longeuer que le message
    for index in range(len(message)):
        result=chr(ord(message[index])^ord(cle[index]))
    return result

decode("ceciestuntest","azertyuiopqsd")