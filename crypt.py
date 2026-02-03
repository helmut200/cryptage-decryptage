message=input("enter the message :")
print(message)
def crypt(message):
    for i in range(len(message)):
        print(( chr(ord(message[i]) + 3)),end="") 
        
crypt(message)


