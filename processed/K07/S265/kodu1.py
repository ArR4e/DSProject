def poisse_ja_tüdrukuid(x):
    p = 0
    t = 0
    for name in x:
        if name[-1] == 'P':
            p += 1
        elif name[-1] == 'T':
            t += 1
    return (p, t)