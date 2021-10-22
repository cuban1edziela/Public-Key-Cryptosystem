import random

def primeGenerator():

    integer = random.randint(100, 1000)
    dev = 2

    while(dev != integer):

        left = integer % dev 

        if(left == 0):                
            integer = random.randint(100, 1000)
            dev = 1
        
        dev = dev + 1
        
        if(dev == integer):
            return integer
