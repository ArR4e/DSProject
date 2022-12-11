def poisse_ja_tüdrukuid(a):
    p = 0
    t = 0
    for i in a:
        if i[-1] == 'P':
            p += 1
        else:
            t += 1
    return (p,t)