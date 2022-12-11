def poisse_ja_tüdrukuid(järjend):
    t = 0
    p = 0
    for element in järjend:
        if element[-1] == 'T':
            t +=1
        elif element[-1] == 'P':
            p +=1
    return (p, t)
