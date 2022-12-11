def poisse_ja_tüdrukuid(jär):
    m=0
    n=0
    for elem in jär:
        if elem[-1]== "T":
            n += 1
        else:
            m+=1
    return (m,n)