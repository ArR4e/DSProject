def poisse_ja_tüdrukuid(inimene):
    poiss=0
    tüdruk=0
    for i in range(len(inimene)):
        a=list(inimene[i])
        if(a[-1]=="P"):
            poiss+=1
        else:
            tüdruk+=1
    return (poiss,tüdruk)