def poisse_ja_tüdrukuid(a):
    
    p = 0
    t = 0
    
    for i in range(len(a)):
        
        n = a[i]
        g = n[-1]
        if g == 'T':
            t += 1
        else:
            p += 1
        i += 1
    return (p, t)