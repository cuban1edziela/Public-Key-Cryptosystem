#Part of the programm which deciphers user's message
#Version 2.2
#Last edit: 22.10.2021
#By Kuba Niedziela



from functions import *                                     #Importing functions and easy changable variables
from constants import *

f = open("keys.txt", "r")
n = int(f.readline())
e_user = int(f.readline())
d = int(f.readline())
f.close()

k_object = k_constant()
k = k_object.constant
l_object = l_constant()
l = l_object.constant


def decipher(user_ciphered_message):

    # Ciphered message is split into 'l' letter ciphertext units.
    # The value of 'l' can be easily changed in 'Variables' folder
    ciphered_message_list = [(user_ciphered_message[i:i+l]) for i in range(0, len(user_ciphered_message), l)]

    deciphered_message = []                                     #'Defining variables for deciphered messages, list holds each letter and string returns a whole word
    deciphered_message_string = ' '

    for i in range(messageLength(user_ciphered_message, l)):    #lopp executes as long as there are ciphered text units
        ciphered_message = ciphered_message_list[i]              #message gets the different, following ciphertext unit to decipher in each loop
        ciphered_number = 0                                      #ciphered number gets value 0 before deciphering another ciphertext unit
        exponent = k - 1                                        #from RSA math theorem, we know that the highest exponent must be exactly 1 less than the number of letters in a plaintext unit
        z = l - 1                                               #similar to the exponent, but this time it has to be 1 less than number of letters in a ciphertext unit

        for x in range(len(ciphered_message)):                  #deciphering each letter at the time by getting its index and calculating ciphered number
            index = alphabet.index(ciphered_message[x])         #detailed information on how the system works can be found in RSA math description on the web
            ciphered_number += (index * (len(alphabet)**z))
            z -= 1                                              #as we get to another letter in ciphertext unit, exponent z gets smaller by 1 at the time

        deciphered_number = pow(ciphered_number, d, n)           #using our key 'd', we decipher the number

        for s in range(k):
            number_multiplicative = len(alphabet)**exponent     #now we do the opposite process of enciphering, from numerical value, we get letters

            q, r = divmod(deciphered_number, number_multiplicative)

            if(q > len(alphabet)):                              #if used numbers are very big (up to 2000 digits on regular RSA Cryptosystem), it may happen that q will exceed number of letters
                q = pow(q, 1, len(alphabet))                    #in the alphabet. Solution to that problem is simply taking mod of q and length of the alphabet

            deciphered_message.append(alphabet[q])              #adding letters into deciphered message list

            deciphered_number = r

            if exponent == 0:
                exponent = k-1
            else:
                exponent -= 1



    for x in deciphered_message:                                #Creating string from the deciphered message list
        deciphered_message_string += x

    return deciphered_message_string

