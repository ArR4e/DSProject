def poisse_ja_tüdrukuid(inimesed):
    emased=0
    isased=0
    for i in inimesed:
        if i[-1:]=="T":
            emased+=1
        else:
            isased+=1
    return (isased,emased)
print(poisse_ja_tüdrukuid(["Lilleke P","Traktor T","Kaevurmesilane T","Puu T","Printsess P","Doktor Krokodill T","Muru T","Seebimull P"]))