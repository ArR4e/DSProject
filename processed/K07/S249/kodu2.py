koju = input("Sisesta teepikkus kilomeetrites: ")

f = open("taksohinnad.txt", encoding = "UTF-8")


taksode_hinnad = []
nimed = []

for rida in f:
    jupid = rida.split(",")
    taksonimi = jupid[0]
    stardi_hind = jupid[1]
    km_hind = jupid[2].strip()
    hind = float(stardi_hind) + float(km_hind)*float(koju)
    taksode_hinnad.append(hind)
    nimed.append(taksonimi)

try:
    odavaim = min(taksode_hinnad)
    takso = int(taksode_hinnad.index(odavaim))
    print("Kõige odavam on " + nimed[takso] +".")
except ValueError:
    print("Palju õnne, kirjuta midagi faili!")



f.close()