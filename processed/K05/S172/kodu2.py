from random import randint

def suurväike(sone):
    #Toome sisse võimalikud kirjavahemärgid
    string = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    #Valime nendest ühe suvalise
    a = randint(0, len(string))
    a = string[a]
    #Kuna ei saa muuta esialgset sõnet, koostame selle baasil uue nimega vastus
    vastus = ''
    
    for i in range(len(sone)):
        x = sone[i]
        #Kui märk on kirjavahemärk, anname selle väärtuse a
        if x in string:
            vastus += a
        #Kui märk on väike täht, teeme seda suureks
        elif x.lower() == x:
            vastus += x.upper()
        #Kui märk on suur täht, teeme seda väiksemaks
        else:
            vastus += x.lower()
    return vastus
            