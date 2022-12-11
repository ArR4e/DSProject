tee = float(input("Sisesta tee pikkus koju: "))
f = open("taksohinnad.txt", "r", encoding="UTF-8")

takso = ()
taksod = []
try:
    for line in f:
        takso = line.strip().split(",")
        taksod.append([(float(takso[1]) + float(takso[2])*tee), takso[0]])
    taksod.sort()
    print("kõige odavam on", taksod[0][1])
except:
    print("tühi fail")