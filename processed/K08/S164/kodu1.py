from random import sample
# b = bingo[1:11]
# i = bingo[1:11]
# n = bingo[1:11]
# g = bingo[11:21]
# o = bingo[11:21]
def genereeri_vahemik(algus, lõpp, arv):
    vahemik = sample(range(algus, lõpp), arv)
    return vahemik

def kontroll(jarjend):
    sisaldab = False
    try:
        if jarjend.index(1) >= 0 and jarjend.index(2) >= 0 and jarjend.index(3) >= 0:
            sisaldab = True        
    except:
       pass 
        
    return sisaldab

def bingo():
    b = genereeri_vahemik(1,11,3)
    
    while True:
        vastus = kontroll(b)
        if vastus == False:
            break
        b = genereeri_vahemik(1,11,3)
    
    c = genereeri_vahemik(11,21,2)
    a = b + c
                
    return a
