import re

def otsikasutaja(fail):
    f = open(fail)
    for rida in f:
        if re.match("\w*http://www.ut.ee/~", rida.strip()):
            kas = re.match('http://www.ut.ee/~(\w*)/', rida.strip())
            kasutaja = kas.group(1)
            print(kasutaja)               
    f.close
                           
otsikasutaja('aadressid.txt')                           