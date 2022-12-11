
def suurväike(lause):
    import string
    import random
    erimärgid = string.punctuation
    erimärk = random.choice(erimärgid)
    lõpplist = []
    lause = list(lause)
    for i in range(0, len(lause)):
        if lause[i] in erimärgid:
            lause[i] = erimärk
        if lause[i].islower() == True:
            lause[i] = lause[i].upper()
            lõpplist += str(lause[i])
        elif lause[i].islower() == False:
            lause[i] = lause[i].lower()
            lõpplist += str(lause[i])
    final = ""        
    for i in lõpplist:
        print(i)
        final += i
    return final
    
    

