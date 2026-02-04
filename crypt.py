from math import *

print("Bienvenue a CDcrypt")
print("choisissez")
print("1-Cryptage")
print("2-Decryptage")
choixo = input("choissez 1 ou 2: ")

# Fonctions de cryptage définies AVANT leur utilisation

def crypt(message):
    """Cryptage César: décalage de 3 caractères"""
    resultat = ""
    for i in range(len(message)):
        resultat += chr(ord(message[i]) + 3)
    return resultat

def crypa(message, a, b):
    """Cryptage Affine: (x * a + b) mod 26"""
    resultat = ""
    for i in range(len(message)):
        resultat += chr((ord(message[i]) * a) + b)
    return resultat

def decrypt(message):
    resultat = ""
    for i in range(len(message)):
        resultat += chr(ord(message[i]) - 3)
    return resultat

def decr_a(message, a, b):
    """Cryptage Affine: (x * a + b) mod 26"""
    resultat = ""
    b=int(b)
    a=int(a)
    for i in range(len(message)):
        resultat += chr(((ord(message[i])) -b) // a)
    return resultat
    
if choixo == '1':
    print("Vous voulez crypter un message.")
    message = input("Entrez le message: ")
    print("Message original:", message)
    
    print("choisissez")
    print("1-Cesar")
    print("2-Affine")
    choix1 = input("Quel code voulez-vous utiliser? ")
    
    if choix1 == '1':
        print("Vous voulez crypter un message avec le code de Cesar")
        message_crypte = crypt(message)
        print("Message crypté:", message_crypte)
    
    elif choix1 == '2':
        print("Vous voulez crypter un message avec le code Affine")
        a = int(input("Saisissez a: "))
        b = int(input("Saisissez b: "))
        message_crypte = crypa(message, a, b)
        print("Message crypté:", message_crypte)
    
    else:
        print("Choix invalide")

elif choixo == '2':
    print("Vous voulez décrypter un message.")
    message=input("veillez saisir le message a decrypter: ")
    print("1- cesar")
    print("2-affine")
    choix1=input("quel code de decodage voulez vous utiliser ? ")
    if choix1=='1':
        message_decry=decrypt(message)
        print("Message decrypte: ",message_decry)

    elif choix1=="2":
        print("vous voulez decrypter avec le code affine")
        a=input("a= ")
        b=input("b= ")
        mess=decr_a(message,a,b)
        print("Message decrypte: ",mess)
    else:
        print("choix invalide")       



    

else:
    print("Choix invalide")

