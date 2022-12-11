f = open("taksohinnad.txt", "r",encoding = "UTF-8")
tee = float(input("Sisesta tepikus: !!kilomeetrites!!"))
hind1=2**99
nimi1 = ""
while True:
    pakkumine = f.readline().strip()
    if pakkumine == "":
        break
    a = pakkumine.split(",")
    hind = float(a[1])+float(a[2])*tee
    nimi = str(a[0])
    if hind<hind1:
        hind1 = hind
        nimi1 = nimi
print("Kõige odavam on " +nimi1+".")