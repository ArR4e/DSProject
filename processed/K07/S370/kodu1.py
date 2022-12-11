def poisse_ja_tüdrukuid(j):
    t=0
    p=0
    
    for el in j:
        if el[-1]=="P":
            p+=1
        elif el[-1]=="T":
            t+=1
    
    return (p, t)
