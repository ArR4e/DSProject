def seosta_lapsed_ja_vanemad(x, y):
    f=open(x)
    f2=open(y)
    sõnastik={}
    sõnastik2={}
    for j in f2:
        j=j.strip()
        sõnastik[j[:11]]=j[12:]
    f2.close()
    
    for i in f:
        if sõnastik[i[12:23]] not in sõnastik2:
            ajutine=[]
            ajutine.append(sõnastik[i[:11]])
        else:
            ajutine=[]
            for j in sõnastik2[sõnastik[i[12:23]]]:
                ajutine.append(j)
            ajutine.append(sõnastik[i[:11]])
        
        ajutine=set(ajutine)
        sõnastik2[sõnastik[i[12:23]]]=ajutine
        
        
    f.close()
    
    sõna=""
    for i in sõnastik2:
        sõna += i +": "
        for j in sõnastik2[i]:
            sõna += str(j)+", "
        print (sõna[:-2])
        sõna=""
    
    return sõnastik2