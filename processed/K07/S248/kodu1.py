def poisse_ja_tüdrukuid(x):
    p=0
    t=0
    for i in x:
        if i[-1:] == "P":
            p+=1
        elif i[-1:] == "T":
            t+=1
        else:
            sugu = (0)
            
    sugu = (p, t)    
    return sugu
        

print (poisse_ja_tüdrukuid([]))
        