def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for i in järjend:
        sugu = i.split(" ")
        if sugu[-1] == "P":
            m += 1
        if sugu[-1] == "T":
            n += 1
                        
    return(m,n)

print(poisse_ja_tüdrukuid([]))


