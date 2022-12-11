import collections

fail = open("filmid.txt")
jarjend = []
koos = []
"märul" == "mГ¤rul"
"õudukas" == "Гµudukas"

for rida in fail:
    koos += rida.splitlines()
    jarjend = [y for x in koos for y in x.split(" - ")]
dikt = dict(zip(jarjend[::2], jarjend[1::2]))
d = collections.defaultdict(list)
for key, value in dikt.items():
    d[value].append(key)
    
def loetleFilmid(zanr):
    def get_keys(dikt, value):
        for zanr, v in d.items():
            while zanr == dikt:
                return v
    if get_keys(dikt, value) == True:
        return get_keys(zanr, value)
    else:
        return None
        
def lisaFilm(l, z):
    with open("filmid.txt", "a") as f:
        f.writelines("\n" + l + " - " + z)
        
def kustutaFilm(k):
    kust = open("filmid.txt", "r")
    lines = kust.readlines()
    kust.close()
    kust = open("filmid.txt", "w")
    for line in lines:
        if k not in line:
            kust.write(line)
    kust.close()

fail.close()