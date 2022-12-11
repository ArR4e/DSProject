from string import punctuation
from random import choice
from re import sub

def suurväike(word):
    punctuation_list = list(punctuation)
    punctuation_list.remove('\\')
    punctuation_list.append(r'\\')
    return sub(f'[{punctuation}]', choice(punctuation_list), word.swapcase())
