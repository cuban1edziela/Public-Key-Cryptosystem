from functions import *
from constants import *

# reading constant keys
f = open("keys.txt", "r")
n = int(f.readline())
e_yours = int(f.readline())
d = int(f.readline())
f.close()


def encipher(message, n, e):
    k_object = k_constant()
    k = k_object.constant
    l_object = l_constant()
    l = l_object.constant

    indicator = k  # indicator gets the number letters in a plaintext unit
    ciphered_message = []  # ciphered message list holds single letters, while ciphered message string will return a whole word
    ciphered_message_string = ' '
    initial_text_number = k - 1  # adding variables to be able to change number 'k' of letters on plaintext unit
    k = initial_text_number

    # dividing user's message into groups of k letters
    message_list = [(message[i:i + indicator]) for i in range(0, len(message), indicator)]

    for i in range(messageLength(message, indicator)):

        message = message_list[
            i]  # enciphering each letter at the time by getting its index and calculating ciphered number
        enciphering_number = 0  # detailed information on how the system works can be found in RSA math description on the web

        for x in range(len(message)):

            index = alphabet.index(message[x])

            enciphering_number = enciphering_number + (index * (len(alphabet) ** k))

            if k == 0:
                k = initial_text_number  # changing the exponent to its initial value if it gets to 0 in case of longer texts
            else:
                k = k - 1

        enciphering_function = pow(enciphering_number, e, n)  # evaluating the enciphering function

        z = l - 1  # new variable 'z' exponent gets value of ciphered text units -1

        for s in range(l):
            q, r = divmod(enciphering_function, (len(alphabet) ** z))

            if q > len(
                    alphabet):  # dividing by remainder number evaluated by enciphering function, then for l letter ciphertext units
                q = pow(q, 1, len(alphabet))

            ciphered_message.append(alphabet[q])
            z = z - 1
            enciphering_function = r

    for x in ciphered_message:
        ciphered_message_string += x

    return ciphered_message_string
