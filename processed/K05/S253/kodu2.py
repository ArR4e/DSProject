from random import randint

temp_string = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def suurväike(sone):
    temp1 = sone.swapcase()
    temp2 = ""
    to_replace = temp_string[randint(0,len(temp_string)-1)]
    for letter in temp1:
        if letter in temp_string:
            temp2 += to_replace 
        else:
            temp2 += letter
    
    return temp2



