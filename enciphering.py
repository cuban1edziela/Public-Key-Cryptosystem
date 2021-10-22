#Part of the programm which enciphers user's message
#Version 2.1
#Last edit: 20.10.2021 
#By Kuba Niedziela

                                      
from Functions import *                                 #Importing functions and easy changable variables
from Variables import *

f = open("keys.txt", "r")
n = int(f.readline())
e_yours = int(f.readline())
d = int(f.readline())
f.close()


#ENCIPHERING PROCESS

# contact_statement = input("Do you want to open a Contactbook? YES/NO")

# if(contact_statement == "YES"):
#     contact_person = input("Enter the contact's name")



message = input("\nEnter your message:")                #User enters message to encipher
e = int(input("Enter the recipent's e number:"))
n = int(input("Enter the recipent's n number:"))










indicator = k                                           #indicator gets the number letters in a plaintext unit
ciphered_message = []                                   #ciphered message list holds single letters, while ciphered message string will return a whole word      
ciphered_message_string = ' '
initialTextNumber = k -1                                #adding variables to be able to change number 'k' of letters on plaintext unit
k = initialTextNumber 

#dividing user's message into groups of k letters
messageList = [(message[i:i+indicator]) for i in range(0, len(message), indicator)]                  


for i in range(messageLength(message, indicator)):

    message = messageList[i]                             #enciphering each letter at the time by getting its index and calculating ciphered number
    encipheringNumber = 0                                #detailed information on how the system works can be found in RSA math description on the web
                                                                     
    for x in range(len(message)):                                  

        index = alphabet.index(message[x])                                                            

        encipheringNumber = encipheringNumber + (index * (len(alphabet)**k))        

        if(k == 0):
            k = initialTextNumber                         #changing the exponent to its initial value if it gets to 0 in case of longer texts 
        else:   
            k = k -1        

    encipheringFunction = pow(encipheringNumber, e, n)    #evaluating the enciphering function

    z = l - 1                                             #new variable 'z' exponent gets value of ciphered text units -1 

    for s in range(l):                                                  
        q, r = divmod(encipheringFunction, (len(alphabet)**z))        

        if(q > len(alphabet)):                            #deviding with remainder number evaluated by enciphering function, then for l letter ciphertext units 
            q = pow(q, 1, len(alphabet))

        ciphered_message.append(alphabet[q])
        z =  z -1 
        encipheringFunction = r


for x in ciphered_message:
    ciphered_message_string += x

print(" \n Your enciphered message is:", ciphered_message_string)

