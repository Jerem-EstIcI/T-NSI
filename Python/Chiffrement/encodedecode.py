def encodecode(message,cle):
    encode=''
    for i in range(len(message)):
        xor=ord(message[i])^ord(cle[i%len(cle)])
        if xor==0:
            lettreCodee=message[i]
        else:
            lettreCodee=chr(xor)
            encode+=lettreCodee
    return encode  

print("cle simple")
encode=encodecode("oui oui oui oui","&6N")
print(encode)
decode=encodecode(encode,"&6N")
print(decode)
print("\n")