def poisse_ja_tüdrukuid(a):
    poisid = 0
    tüdrukud = 0
    for inimesed in a:
        if inimesed[-1] == "P":
            poisid += 1
        elif inimesed[-1] == "T":
            tüdrukud += 1
        else:
            print("error")
    return (poisid, tüdrukud)
