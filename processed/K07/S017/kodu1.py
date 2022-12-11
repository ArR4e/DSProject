def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for i in järjend:
        if i[-1] == "P":
            m += 1
        if i[-1] == "T":
            n += 1
    return (m, n)

print(poisse_ja_tüdrukuid(["Mati P", "Kati T", "Siim Aleksander P", "Jüri P", "Veronika T"]))
