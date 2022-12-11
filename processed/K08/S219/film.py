def loetleFilmid(žanr):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()
    
    žanr_list = []
    
    for rida in read:
        if rida.endswith(žanr + "\n") or rida.endswith(žanr):
            nimi = rida.split(' - ')[0]
            žanr_list = žanr_list + [nimi]
    return(žanr_list)

def lisaFilm(nimi, žanr):
    with open("filmid.txt") as f:
        tekst = f.read()
    with open("filmid.txt", "a") as f:
        if not tekst.endswith('\n'):
            f.write('\n')
        f.write(nimi + " - " + žanr + '\n')
    
def kustutaFilm(nimi):
    with open("filmid.txt", "r") as f:
        read = f.readlines()
    with open("filmid.txt", "w") as f:
        for rida in read:
            filminimi = rida.split(' - ')[0]
            if filminimi != nimi:
                f.write(rida)