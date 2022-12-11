def poisse_ja_tüdrukuid(järjend):
    n = 0
    m = 0
    if len(järjend) != 0:
        for el in järjend:
            if  el[-1] == 'P':
                n +=1
            else:
                m +=1
        return (n,m)
    else:
        return (n,m)
    
