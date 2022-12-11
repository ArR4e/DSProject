import film

def töötleKäsk(käsk, järj):
    if käsk == 'K':
        for i in film.loetleFilmid(järj[0]):
            print(i)
    if käsk == 'L':
        film.lisaFilm(järj[1], järj[0])
        print('Film lisatud!')
    if käsk == 'V':
        film.kustutaFilm(järj[0])
        print('Film nimekirjast kustutatud!')
            
while True:
    sisend = str(input('Sisesta käsk: '))
    käsk = sisend.split()[0]
    
    if käsk == 'E':
        break
    
    if käsk == 'V':
        järj = sisend.split(' ', 1)[1:]
    else:
        järj = sisend.split(' ', 2)[1:]
       
    töötleKäsk(käsk, järj)
    