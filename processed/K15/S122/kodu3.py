from datetime import datetime

fail = input("Sisesta failinimi: ")
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")


with open(fail) as f:
    sõitude_kestused = []
    for rida in f:
        rida_korras = rida.strip().split(" ")
        väljumine = rida_korras[0]
        saabumine = rida_korras[1]
        aeg = "%H:%M"
        sõit = (datetime.strptime(saabumine,aeg)-datetime.strptime(väljumine,aeg))
        sõit = int(sõit.total_seconds())
        sõitude_kestused.append(sõit)

    lühim_sõit = min(sõitude_kestused)

with open("sõiduplaan.txt") as f:
    for rida in f:
        rida_korras = rida.strip().split(" ")
        väljumine = rida_korras[0]
        saabumine = rida_korras[1]
        aeg = "%H:%M"
        sõit = (datetime.strptime(saabumine,aeg)-datetime.strptime(väljumine,aeg))
        sõit = int(sõit.total_seconds())
        if sõit == lühim_sõit:
            print(rida)
