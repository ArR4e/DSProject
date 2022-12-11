def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    b =len(järjend)
    if b == 0:
        return(0)
    for rida in järjend:
        uus_järjend = rida.split(" ")
        a = uus_järjend[-1]
        if a == "P":
            m+=1
            b-=1
        if a == "T":
            n+=1
            b-=1
        if b < 1:
            return(m, n)
            break
        else:
            continue