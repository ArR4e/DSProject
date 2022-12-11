def poisse_ja_tüdrukuid(järjend):
    poiss=0
    tüdruk=0
    järjend = ' '.join(järjend).split()
    for el in järjend:
        if el== 'P':
            poiss+=1
        if el=='T':
            tüdruk+=1
    ennik=(poiss,tüdruk)
    return ennik
