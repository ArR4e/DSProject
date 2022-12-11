def poisse_ja_tüdrukuid(järjend):
    jrd = []
    if len(järjend) == 0:
        return (0, 0)
    for s in järjend:
        t = s[-1]
        jrd.append(t)
    poisse = jrd.count("P")
    tüdrukuid = jrd.count("T")
    return(poisse, tüdrukuid)

järjend = str(input("Sisestage oma järjend: "))
print(poisse_ja_tüdrukuid(järjend))