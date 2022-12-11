def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for sõne in järjend:
        if sõne[-1] == 'P':
            poisid += 1
        elif sõne[-1] == 'T':
            tüdrukud += 1
    return (poisid, tüdrukud)

inimesed = ['Mati P', 'Siim Aleksander P', 'Jüri P']

print(poisse_ja_tüdrukuid(inimesed))