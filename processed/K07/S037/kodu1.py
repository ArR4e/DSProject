def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for el in järjend:
        el = el[-1]
        if el == 'P':
            m +=1
        elif el == 'T':
            n += 1
    return (m,n)
    
