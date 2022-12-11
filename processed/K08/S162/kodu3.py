import film
def töötleKäsk(tähis, parameetrid):
    if tähis=='K':
        if film.loetleFilmid(parameetrid[0])==[]:
            print('Sellest žanrist pole ühtki filmi, vali uus žanr')
        else:
            print('Võimalikud filmid on:')
            for i in film.loetleFilmid(parameetrid[0]):
                print(i)
        return True
    if tähis=='L':
        film.lisaFilm(parameetrid[1],parameetrid[0])
        print('Film lisatud!')
        return True
    if tähis=='V':
        film.kustutaFilm(parameetrid[0])
        print('Film nimekirjast kustutatud! Head vaatamist :)')
        return True
    if tähis =='E':
        return False
a=input('')
a1=a.split()[0]
a2=a.split()[1:]
while töötleKäsk(a1,a2)==True:
    a=input('')
    a1=a.split()[0]
    a2=a.split()[1:]
