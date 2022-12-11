f = open("taksohinnad.txt", "r")
s = float(input("Sisesta teepikkus kilomeetrites: "))
hinnad = []
nimed = []
for rida in f:
    jrj = rida.replace("\n", "").split(",")
    kmhind = float((jrj[2]))
    hind = float(jrj[1]) + kmhind * s
    hinnad.append(hind)
    nimed.append(jrj[0])
try:
    takso = nimed[hinnad.index(min(hinnad))]
    print("Kõige odavam on", takso +".")
    f.close()
except:
    print("Teepikkus ei sobi.")