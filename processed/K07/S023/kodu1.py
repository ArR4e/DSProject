
list1 = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid(list1):
    p = 0
    t = 0
    for i in list1:
        if i[-1] == "P" or i[-1] == "p":
            p = p + 1
        elif i[-1] == "T" or i[-1] == "t":
            t = t + 1
    return (p,t)

print(poisse_ja_tüdrukuid(list1))