import random
low = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
other='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
upper = 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
word=input('kirjutage siia lause: ')
def suurväike (word):
    sona=''
    for i in word:
        if i in low:
            i=i.upper()
            sona=sona+ i
        elif i in upper:
            i=i.lower()
            sona=sona+ i
        elif i in other:
            otherList=list(other)
            
            i=random.choice(otherList)#ei ole kindel kas peab olema random v sain ise valida suvalt selle
            
            sona=sona+ i
        else:
            i=' '
            sona=sona+ i
    return(sona)
print(suurväike(word))
    