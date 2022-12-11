aastatulu=float(input(print("Mis on sinu aasta bruto sissetulek: ?")))
esimene=round(aastatulu, 2)
teine_1=float(aastatulu-6000)
teine_2=float(aastatulu-teine_1)
teine_3=round(teine_2, 2)
kolmas_1=float((6000-((6000/10800)*(float(aastatulu)-14400))))
kolmas_2=round(kolmas_1, 2)
if aastatulu<=6000:
    print(esimene)
if aastatulu>6000 and aastatulu<=14400:
    print(teine_3)
if aastatulu>14400 and aastatulu<=25200:
    print(kolmas_2)
if aastatulu>25200:
    print(0)