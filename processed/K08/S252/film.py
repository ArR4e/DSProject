failiNimi = "filmid.txt"

def loetleFilmid(zanr):
    loetelu = []
    with open(failiNimi) as file:
        for line in file:
            tmpVal = line.rstrip()
            arr = tmpVal.split(" - ")
            print(arr[1])
            if arr[1] == zanr:
                loetelu.append(arr[0])
    return loetelu

def lisaFilm(nimi,zanr):
    with open(failiNimi,"a") as file_object:
        file_object.write("\n"+nimi+"-"+zanr)
        return
    
def kustutaFilm(nimi):
    loetelu = []
    with open (failiNimi) as file:
        for line in file:
            tmpVal = line.rstrip()
            arr = tmpVal.split(" - ")
            print(arr[1])
            if arr[0] != nimi:
                loetelu.append(tmpVal)
    i = 0
    with open(failiNimi,"w") as file_object:
        while i < len(loetelu):
            if i > 0:
                file_object.write(loetelu[i])
                print(loetelu[i])
                i += 1
    return

lisaFilm("Nukitsamees","märul")
print(loetleFilmid("märul"))
kustutaFilm("Moana")
print(loetleFilmid("märul"))