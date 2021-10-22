#Part of the programm which deciphers user's message
#Version 2.1
#Last edit: 20.10.2021 
#By Kuba Niedziela



from Functions import *                                     #Importing functions and easy changable variables
from Variables import *

f = open("keys.txt", "r")
n = int(f.readline())
e_user = int(f.readline())
d = int(f.readline())
f.close()


user_ciphered_message = input("Enter a message you want to decipher: ")                   
# n = int(input("\n Enter the 'n' value of the key:"))        #User enters required information: ciphered message and two values of the key
# d = int(input("\n Enter the 'd' value of the key:"))


#Ciphered message is splited into 'l' letter ciphertext units. 
#The value of 'l' can be easly changed in 'Variables' folder
ciphered_messageList = [(user_ciphered_message[i:i+l]) for i in range(0, len(user_ciphered_message), l)] 


deciphered_Message = []                                     #Defining variables for deciphered messages, list holds each letter and string returns a whole word
deciphered_message_string = ' '

for i in range(messageLength(user_ciphered_message, l)):    #lopp executes as long as there are ciphered text units     
    ciphered_message = ciphered_messageList[i]              #message gets the different, following ciphertext unit to decipher in each loop 
    cipherednumber = 0                                      #ciphered number gets value 0 before deciphering another ciphertext unit
    exponent = k - 1                                        #from RSA math theorem, we know that the highest exponent must be exactly 1 less than the number of letters in a plaintext unit
    z = l - 1                                               #similar to the exponent, but this time it has to be 1 less than number of letters in a ciphertext unit
    

    for x in range(len(ciphered_message)):                  #deciphering each letter at the time by getting its index and calculating ciphered number
        index = alphabet.index(ciphered_message[x])         #detailed information on how the system works can be found in RSA math description on the web
        cipherednumber += (index * (len(alphabet)**z))
        z -= 1                                              #as we get to another letter in ciphertext unit, exponent z gets smaller by 1 at the time


    deciphered_number = pow(cipherednumber, d, n)           #using our key 'd', we decipher the number 


    for i in range(k):
        number_multiplicative = len(alphabet)**exponent     #now we do the opposite process of enciphering, from numerical value, we get letters

        q, r = divmod(deciphered_number, number_multiplicative)

        if(q > len(alphabet)):                              #if used numbers are very big (up to 2000 digits on regular RSA Cryptosystem), it may happen that q will exceed number of letters 
            q = pow(q, 1, len(alphabet))                    #in the alphabet. Solution to that problem is simply taking mod of q and length of the alphabet

        deciphered_Message.append(alphabet[q])              #adding letters into deciphered message list

        deciphered_number = r

        if(exponent == 0):
            exponent = k-1
        else:
            exponent -= 1

for x in deciphered_Message:                                #Creating string from the deciphered message list 
    deciphered_message_string += x

print("\n Deciphered message is", deciphered_message_string)   
