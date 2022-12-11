a = float(input("Sisesta tee pikkus kilomeetrites:"))
f = open("taksohinnad.txt","r",encoding="utf-8'")
d = {}

for i in f:
    lst = i.strip("\n").split(",")
    d[lst[0]]= (float(lst[1])+(float(lst[2]))*a)
f.close()
try:
    key_min = min(d.keys(), key=(lambda k: d[k]))
    print("Kõige odavam on " + key_min +".")
except:
    print("0")
