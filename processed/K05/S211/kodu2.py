import string
import random




def suurväike(argument):
    
    uus_märk = str(random.choice(string.punctuation))
    print(uus_märk)
    
    for märk in argument:
        
        if märk in string.punctuation:
            argument = argument.replace(märk, uus_märk)
    
    uus_case = str.swapcase(argument)
            
    return(uus_case)
    