kodutee = float(input("Sisesta kodutee pikkus kilomeetrites:"))
f = open("taksohinnad.txt", encoding = "UTF-8")
t1 = f.readline().strip().split(",")
t2 = f.readline().strip().split(",")
t3 = f.readline().split(",")
nimi1 = t1[0]
nimi2 = t2[0]
nimi3 = t3[0]
stardihind1 = t1[1]
stardihind2 = t2[1]
stardihind3 = t3[1]
kilomeetrihind1 = t1[2]
kilomeetrihind2 = t2[2]
kilomeetrihind3 = t3[2]
def maksumus1(start, tee, kodutee, pakkuja):
    start1 = float(start)
    tee1 = float(tee)
    kulub1 = start1 + tee1*kodutee
    return kulub1
def maksumus2(start, tee, kodutee, pakkuja):
    start1 = float(start)
    tee1 = float(tee)
    kulub2 = start1 + tee1*kodutee
    return kulub2
def maksumus3(start, tee, kodutee, pakkuja):
    start1 = float(start)
    tee1 = float(tee)
    kulub3 = start1 + tee1*kodutee
    return kulub3
list = []
list.append(maksumus1(stardihind1, kilomeetrihind1, kodutee, nimi1))
list.append(maksumus2(stardihind2, kilomeetrihind2, kodutee, nimi2))
list.append(maksumus3(stardihind3, kilomeetrihind3, kodutee, nimi3))

väikseim = min(list)
if väikseim == maksumus1(stardihind1, kilomeetrihind1, kodutee, nimi1):
    print("Kõige odavam on ", nimi1+ ".")
elif väikseim == maksumus2(stardihind2, kilomeetrihind2, kodutee, nimi2):
    print("Kõige odavam on ", nimi2+ ".")
elif väikseim == maksumus3(stardihind3, kilomeetrihind3, kodutee, nimi3):
    print("Kõige odavam on ", nimi3+ ".")