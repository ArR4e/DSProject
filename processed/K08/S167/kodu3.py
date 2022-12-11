#jukufilmiandmebaas
#eelnevad pythoni programmid saavad ka moodulitena käituda, hoides alamprogramme def funktsioonis.
import film

print("FILMIANDMEBAAS")
print("Kuva filmid: K <žanr>")
print("Lisa film: L <žanr, film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta: E")



def töötleKäsk(tähis, järjend):           
    stringK = ""
    if tähis == "K":
        for i in järjend:
            stringK += i
        print("Võimalikud filmid on:")
        for i in film.loetleFilmid(stringK):
            print(i)
    
    
    stringL1 = ""
    stringL2 = ""
    if tähis == "L":
        i1 = 0
        for i in järjend:
            if i == " ":
                break
            stringL1 += i
            i1 += 1
        i1 +=1
        while i1<len(järjend):
            d = järjend[i1]
            stringL2 += d
            i1 += 1
        film.lisaFilm(stringL2, stringL1)
        print("Film lisatud!")
    
    
    stringV = ""
    if tähis == "V":
        for i in järjend:
            stringV += i
        film.kustutaFilm(stringV)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    
    
    if tähis != "E":
        f = tähis == "E"
        return f
    
    if tähis == "E":
        f = tähis != "E" 
        return f
while True:
    a = input("")
    
    list = []
    for i in a:
        list.append(i)
        
    tähis = list[0]
    
    järjend = list.copy()
    
    if tähis != "E":
        järjend.pop(0)
        järjend.pop(0)
    
    
    töötleKäsk(tähis, järjend)
    if a == "E":
#        print(töötleKäsk(tähis, järjend))
        exit()