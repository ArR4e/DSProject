import film

def töötleKäsk(tähis, järjend):
    
    if tähis == 'K':
        film.loetleFilmid(järjend[1])
        
    if tähis == 'L':
        if len(järjend) == 4:
            järjend = sisestus.split(' ', 2)
            film.lisaFilm(järjend[2], järjend[1])
            
        elif len(järjend) == 3:
            järjend = sisestus.split(' ')
            film.lisaFilm(järjend[2], järjend[1])
        
    if tähis == 'V':
        if len(järjend) == 3:
            järjend = sisestus.split(' ', 1)
            film.kustutaFilm(järjend[1])
            
        elif len(järjend) == 2:
            järjend = sisestus.split(' ')
            film.kustutaFilm(järjend[1])
    
while True:
    sisestus = input('Sisestus: ')
    tähis = sisestus.split(' ')[0]
    järjend = sisestus.split(' ')
    
    if tähis == 'E':
        break
    
    töötleKäsk(tähis, järjend)