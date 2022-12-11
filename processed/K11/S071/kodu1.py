# 11.1. Lapsed ja vanemad (kodu1)
# lapsed.txt ---> vanema_ID lapse_ID
# nimed.txt ----> ID nimi
# korduvaid nimesid ei esine & igale lapsed.txt ID jaoks on vastav nimi olemas

# väljastab nimi: {ema, isa}
def seosta_lapsed_ja_vanemad(laste_fail,nimede_fail):
    f1 = open(laste_fail,"r")
    f2 = open(nimede_fail, "r")
    seosed = set()
    lapsed = []
    lapsed = f1.read().split()
    nimed = f2.read().split()
    f1.close()
    f2.close()
    
    i = 0
    while i <= 6:
        seosed[lapsed[i]] = lapsed[i+1]
        i += 1
        
    print(lapsed)
    print(nimed)
    print(seosed)
    #return sõnastik # lapse nimi: {vanemad}

print(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))