from constants import *
from functions import *                                 #Importing functions and easy changable variables
from classes import *

f = open("keys.txt", "r")
n = int(f.readline())
e_yours = int(f.readline())
d = int(f.readline())
f.close()


# class encipher_message(message):
#     def __init__(self, message_content, n, e):
#         super().__init__(message_content)
#         self.n = n
#         self.e = e

#     def encipher(message_content, n, e):
#         import enciphering
