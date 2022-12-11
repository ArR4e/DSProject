import re
def loe(fail):
    f = open(fail, 'r', encoding = 'UTF-8')
    
    for a in f:
        a = a.strip()
        #print(a)
        kasutaja = re.search('www.ut.ee/~(\w+)/', a)
        if kasutaja != None:
            print(kasutaja.group(1))
        else:
            continue
        
        
        
loe('aadressid.txt')
        