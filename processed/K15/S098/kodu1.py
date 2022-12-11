import re
def regulaaravaldis():
    
    d = 0
    f = 0
    G = ''
    
    TEKST = open('aadressid.txt', encoding = 'UTF-8')
    for rida in TEKST:
        if re.search('ut', rida):
            if re.search('~..../', rida):
                a = rida.split('~')
                b = list(a[1])
                c = b.index('/')
                
                while d<c:
                    h = G+(b[f])
                    f +=1
                    d +=1
                    
                    
                    
                sõna = re.search('~..../', rida)
                print(h)#(rida)
regulaaravaldis()