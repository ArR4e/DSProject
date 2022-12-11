def loetleFilmid(žanr):
    fail = open("filmid.txt", "r", encoding = "UTF-8")
    järjend = []
    for rida in fail:
        film, žanr1 = rida.strip("\n").split(" - ")
        if žanr == žanr1:
            järjend.append(film)
    fail.close()
    return järjend

def lisaFilm(film, žanr):
    fail = open("filmid.txt", "r+")
    järjend = " " + film + " - " + žanr
    while True:
        if fail.readline()!= "":
            continue
        else:
            fail.write("\n")
            fail.write(järjend)
            break
    fail.close()
    
def kustutaFilm(film):
    fail = open("filmid.txt", "r+")
    read = fail.readlines()
    fail.close()
    järjend = open("filmid.txt", "w+")
    for el in read:
        if film in el:
            read.remove(el)
    järjend.writelines(read)
    järjend.close()
    

    


        
# def loetleFilmid(žanr)
# print(loetleFilmid)
    
    
# tagastab järjendi kõikide filmidega

# def lisaFilm(nimi, žanr)
# peab faili lisama soovitud filmi+žanr
# nimi-žanr

# def kustutaFilm(nimi)
# kustutab tekstifailist ära
