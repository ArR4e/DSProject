def poisse_ja_tüdrukuid(nimed):
    summa1 = 0
    summa2 = 0
    for el in nimed:
        if el.endswith("P"):
            summa1 += 1
        if el.endswith("T"):
            summa2 += 1
    return (summa1, summa2)