järjend = input("Sisestage järjend: ")

def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for el in järjend:
        if el == '':
            continue
        else:
            sugu = el[-1]
            if sugu == 'P':
                poisse += 1
            elif sugu == 'T':
                tüdrukuid += 1
    return (poisse, tüdrukuid)

print(poisse_ja_tüdrukuid(järjend))
        