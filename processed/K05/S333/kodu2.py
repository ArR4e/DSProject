import string
import random

def suurväike(sõne) :
    
    sõne= sõne.swapcase() #vahetab tähed ära
    sümbolid= (string.punctuation) #tagastab kõik kirjavahemärgid
    lõpp= len(string.punctuation)-1 #miinus üks,sest loendus algab nullist
    juhus= random.randint(0,lõpp) #leiab juhusliku numbri märkides
    #juhus enne for tsüklit tagastab ühe sümboli, tsükli sees iga asendus uus
    
    for märk in sõne:
        if märk in sümbolid:
            sõne= sõne.replace(märk,sümbolid[juhus]) #asendab juhusliku mängiga
    
    
    return sõne
