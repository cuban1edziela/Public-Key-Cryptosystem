import random




def coprimeChecker(k):

    gcd = 0

    while(gcd != 1):

        intA = k                              #generate a random number. range must be changed at least 2k digit number 
        intB = random.randint(1, 1000)

        remainder = (intA % intB) 
        a = remainder
        b = intB

        if(remainder != 0):                                           #for numbers when a mod b is not equal to 0

            while(remainder > 0):
                
                remainder = (b % a)
                b = a

                if(remainder == 0):
                    gcd = a             
                
                a = remainder
        
        else:
            intB = random.randint(1, 1000)


    return intB