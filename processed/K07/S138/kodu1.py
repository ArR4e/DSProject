def poisse_ja_tüdrukuid(nimekiri):
    nim = [z[-1] for z in nimekiri]
    x = 0
    y = 0
    for i in nim:
        if i == "P":
            x+=1
        elif i == "T":
            y+=1
    return x,y