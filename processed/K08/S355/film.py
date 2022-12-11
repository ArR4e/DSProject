def loetleFilmid(zanr):
    global filminimi
    filminimi = []
    avafail = open("filmid.txt", "r", encoding='utf-8')
    filmid = avafail.readlines()
    for rida in filmid:
        rida = rida.strip().split(" - ")
        filmiliik = rida[-1]
        if filmiliik == zanr:
            filminimi.append(rida[0])
    return filminimi  
    
    
def lisaFilm(zanr, filminimi):
    with open("filmid.txt", "a", encoding='utf-8') as kirjutamine:
        kirjutamine.write('\n'+ filminimi + " - " + zanr)
    print("Film on lisatud.")

def kustutaFilm(filminimi):
    loefail = open("filmid.txt", "r", encoding='utf-8')
    lugemine = loefail.readlines()
    liitja = 0
    listboi = []
    while True:
        try:
            film = lugemine[liitja].strip().split(" - ")
            liitja +=1
            listboi += film
        except:
            break 
    
    if filminimi in listboi:
        listiindex = listboi.index(filminimi)
        del listboi[listiindex:listiindex+2]
    
    pealkirjad = listboi[::2]
    zanrinimed = listboi[::-2]
    zanrinimed = zanrinimed [::-1]
    listfinaal = []
    string = ""
    
    for el,elem in zip(pealkirjad, zanrinimed):
        el += " - "
        elem += '\n'
        string += el
        string+= elem
        
    kirjutamine = open("filmid.txt", "w", encoding = 'utf-8')
    kirjutamine.write(string)
    print("Film on kustutatud")        
    




# elif valik == "lisada filmi":
#     filminimi = input("Vali filmi nimi: ")
#     zanr = input("Vali zanr: ").lower()
#     lisaFilm(filminimi, zanr)
# elif valik == "kustutada filmi":
#     filminimi = input("Vali filmi nimi: ")
#     kustutaFilm(filminimi)
# else:
#     print("Proovi uuesti - sellist funktsiooni ei ole")

