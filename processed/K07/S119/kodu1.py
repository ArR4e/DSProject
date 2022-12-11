def poisse_ja_tüdrukuid(järjend):
    t = 0
    p = 0
    for el in järjend:
        if el[-1] == "T":
            t = t + 1
        if el[-1] == "P":
            p = p + 1
    return (p, t)

       

        
        
nimed = ['Mati P', 'Kati P', 'Siim Aleksander P', 'Jüri P', 'Veronika P']
print(poisse_ja_tüdrukuid(nimed))



