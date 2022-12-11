def poisse_ja_tüdrukuid(a):
    m=0
    n=0
    for nimi in a:
        b=nimi.split()
        c=len(b)-1
        if b[c]=="P":
            m+=1
        else:
            n+=1
    return (m,n)

        