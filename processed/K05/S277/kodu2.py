import string
from random import randint
def suurväike(sõne):
    sõne1 = ''
    for i in sõne:
        a = 0
        if i is ' ':
            sõne1 += ' '
            continue
        if i.isalpha() is not True:
            while i is not list(string.punctuation)[a]:
                a += 1
            if i is list(string.punctuation)[a]:
                sõne1 += i.replace(list(string.punctuation)[a], list(string.punctuation)[randint(0, 33)])
                continue
        else:
            while i is not list(string.ascii_uppercase)[a] and i is not list(string.ascii_lowercase)[a]:
                a += 1
            if  i is list(string.ascii_uppercase)[a]:
                sõne1 += i.replace(list(string.ascii_uppercase)[a], list(string.ascii_lowercase)[a])
            elif i is list(string.ascii_lowercase)[a]:
                sõne1 += i.replace(list(string.ascii_lowercase)[a], list(string.ascii_uppercase)[a])
    return sõne1
print(suurväike('!!!!!!!'))