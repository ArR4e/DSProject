import string
from random import choice

def suurväike(input_str):
    output = ''
    random_symbol = choice(string.punctuation)
    for letter in input_str:
        
        if letter in string.punctuation:
            output += random_symbol
        elif letter.upper() == letter:
            output += letter.lower()
        else:
            output += letter.upper()

    return output
