def poisse_ja_tüdrukuid(andmed):
    poisse=0
    tüdrukuid=0
    for tekst in andmed:
        jupid=tekst.split()
        if jupid[-1]=="P":
            poisse+=1
        else:
            tüdrukuid+=1
    return (poisse,tüdrukuid)

#print(poisse_ja_tüdrukuid([]))