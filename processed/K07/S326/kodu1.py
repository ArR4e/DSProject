def poisse_ja_tüdrukuid(järjend):
    p = 0
    t = 0
    for i in järjend:
        ijärjend = i.split(" ")
        if "T" in ijärjend:
            t += 1
        elif "P" in ijärjend:
            p += 1
    return (p, t)

    