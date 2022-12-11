def arvuta(sisse, kmhind, km):
    lopp = round(sisse + kmhind * km, 2)
    return lopp

f = open("taksohinnad.txt", encoding = "utf-8")
takso = []
k = 0
taksosid = 0
hinnad = []
read = f.readlines()
f.close()

while k < len(read):
    a = read[k].strip().split(",")
    takso.append(a)
    k+=1
    taksosid += 1
k = 0
km = float(input("Sisestage tee pikkus kilomeetrites: "))

while taksosid > k:
    hinnad.append(arvuta(float(takso[k][1]),float(takso[k][2]),km))
    k+=1
k = 0
k = hinnad.index(min(hinnad))
print("Kõige odavam on " + str(takso[k][0]) + ".")