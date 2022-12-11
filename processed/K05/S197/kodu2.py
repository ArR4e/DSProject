from random import randint
import string

def suurväike(line):
    new_line = ''
    line = line.swapcase() #Vahetame tähtede suurused
    rand_punct = string.punctuation[randint(0, 31)] #Valime juhusliku sümboli
    for i in line:
        if i in string.punctuation:
            i = rand_punct #Vahetame sümboli
        new_line += i
    return new_line