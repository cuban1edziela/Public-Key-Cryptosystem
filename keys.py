from Functions import *
from Variables import *




keys = open("keys.txt","w+")



#ENCIPHERING KEY (PUBLIC)              
p_1 = primeGenerator()                                  #randomly generating two prime numbers 'p, q' and two numbers 'e' coprime to their values -1
q_1 = primeGenerator()
ep = coprimeChecker((p_1 - 1))
eq = coprimeChecker((q_1 - 1))

while(ep != eq):                                        #from RSA math theorem, we know that number 'e' must be coprime to both 'p' and 'q' numbers less than 1
    p_1 = primeGenerator()                              #in this loop, numbers are generated unitl the number 'e' is found 
    q_1 = primeGenerator()
    ep = coprimeChecker((p_1 - 1))
    eq = coprimeChecker((q_1 - 1))

n = (p_1 * q_1)                                         #again, from RSA math theorem, we know that number n is (p*q), so we calculate 'n'
e = ep                                                  #now 'ep' is substituted to the variable 'e' which will be used later on 

#--------------------------------------------------------

#DECIPHERING KEY (SECRET)
phi_of_n = (p_1 - 1) * (q_1 - 1)                        #calculating the Euler's function for number 'n'. 'p' and 'q' are prime hence we can calculate the function by multiplying their values -1                                                

d = pow(e, (-1), phi_of_n)                              #from RSA math theorem, we have to calculate the inverse of 'e' mod phi of n, (Euler's function of n)

keys.write(str(n) + "\n" +str(e) + "\n" + str(d))


keys.close()