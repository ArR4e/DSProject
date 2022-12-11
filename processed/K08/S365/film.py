info = ""
with open("filmid.txt", 'r', encoding= "utf-8") as f:
    info = f.readlines()
    
m = open("filmid.txt", 'w', encoding= "utf-8")

def main():
    küsimus = str(input("mis zanrit tahad kontrollida? "))
    lisa_nimi = str(input("lisa filmi nimi :"))
    lisa_zanr = str(input("lisa filmi zanr :"))
    kustuta_nimi = str(input("mis nime tahad kustutada :"))
    info = ""
    with open("filmid.txt", 'r', encoding= "utf-8") as f:
        info = f.readlines()
    
    m = open("filmid.txt", 'w', encoding= "utf-8")
    lisaFilm(lisa_nimi, lisa_zanr)
    kustutaFilm(kustuta_nimi)
    m.close()
    print(loetleFilmid(küsimus)) 

def lisaFilm(lisa_nimi, lisa_zanr):
    uus_nimi = str(str(lisa_nimi)+ " - "+ str(lisa_zanr))
    m.write("\n")
    m.write((uus_nimi))
    for x in info:
        x=x.strip()
        m.write(x)
        m.write("\n")
    m.close()

def loetleFilmid(küsimus):
    järjend = []
    for x in info:
        x = x.strip().split(' - ')
        uus = (küsimus)   
        if uus == x[1]:
            järjend.append(x[0])
    return järjend

def kustutaFilm(kustuta_nimi):
    for x in info:
        x = x.strip().split(' - ')
        if x[0] != kustuta_nimi:
            m.write(x[0])
            m.write(' - ')
            m.write(x[1])
            m.write("\n")
        m.close()

if __name__ == "__main__":
    main()