#masintõlge

#küsi failinimed

esimene_fail_nimi = input("Sisesta esimene failinimi: ")

teine_fail_nimi = input("Sisesta teine failinimi: ")



esimene_fail = open(esimene_fail_nimi, "r")
data = esimene_fail.read()
esimene_fail.close()

teine_fail = open(teine_fail_nimi, "a+")
teine_fail.write(data)
asendamised = data.count("Hello")
teine_fail.close()

import re

with open(teine_fail_nimi, "r+") as f:
    text = f.read()
    text = re.sub("Hello", "Tere", text)
    f.seek(0)
    f.write(text)
    f.truncate()
    
print("Asendamisi tehti: ")

print(asendamised)

