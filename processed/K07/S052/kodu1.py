järjend = ["Mati P", "Kati T", "Peeter P", "Ants P"]

def poisse_ja_tüdrukuid(järjend):
    i = 0
    poisse = 0
    tüdrukuid = 0
    while i < len(järjend):
        element = järjend[i]
        if " P" in element:
            poisse += 1
            i += 1
            continue
        elif " T" in element:
            tüdrukuid += 1
            i += 1
            continue
        else:
            continue
        i += 1
    ennik = (poisse, tüdrukuid)
    return ennik
poisse_ja_tüdrukuid(järjend)
