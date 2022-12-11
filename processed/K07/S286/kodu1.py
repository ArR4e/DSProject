
def poisse_ja_tüdrukuid(järjend):
    tüdrukuid = 0
    poisse = 0
    for x in range(len(järjend)):
        element = järjend[x]
        a = element[::-1]
        if a[0] == "P":
            poisse +=1
        if a[0] == "T":
            tüdrukuid += 1
    return(poisse, tüdrukuid)
järjend = ["Mati P","Kati T","Siim Aleksander P","Veronika T"]
x = poisse_ja_tüdrukuid(järjend)
