fail = open("bussid.txt", "r")
väljumised = []
saabumised = []
hinnad = []

def vali_sobiv(fail):
    for rida in fail:
        rida = rida.strip().split(" ")
        väljumisaeg = rida[0]
        väljumised.append(väljumisaeg)
        saabumisaeg = rida[1]
        saabumised.append(saabumisaeg)
        hind = rida[3]
        hinnad.append(hind)
        
print(vali_sobiv(fail))
