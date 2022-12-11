def loetleFilmid(zanr):
    filmi_jarjend = []
    
    with open('filmid.txt') as f:
        for rida in f:
            if rida.split(' - ')[1].strip() == zanr:
                filmi_jarjend.append(rida.split('-')[0].strip())
    
    return filmi_jarjend
                
def lisaFilm(nimi, zanr):
    with open('filmid.txt', 'a') as f:
        f.write(f'\n{nimi} - {zanr}')

def kustutaFilm(nimi):
    with open('filmid.txt', 'r') as f:
        filmid = f.readlines()
        filmid = [film for film in filmid if film.split('-')[0].strip() != nimi]
        
    with open('filmid.txt', 'w') as f:
        f.writelines(filmid)
