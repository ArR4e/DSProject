def moos(suur, vaike , moosikogus):
    x = 0
    while True:
        if moosikogus >= 5 and suur >= 1:
            suur -= 1
            moosikogus -= 5
            x += 1
        elif moosikogus >= 1 and vaike >= 1:
            vaike -= 1
            moosikogus -= 1
            x += 1
        else:
            break
    if moosikogus > 0:
        x = -1
    return x