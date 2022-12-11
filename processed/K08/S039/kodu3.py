from film import loetleFilmid,lisaFilm,kustutaFilm
käsk1='K märul'#input("Kuva filmid: ")
käsk2='L komöödia Borat'#input("Lisa film: ")
käsk3='V Avengers: End Game'#input("Vaata filmi: ")
käsk4='E'#input("Lõpeta: ")

parameeter1=käsk1.split()#siia peaks kõik käsud korraga saama kuidagi
tähis=parameeter1[0]
argument=parameeter1[1]
def töötleKäsk(tähis,argument):
    import film
    if tähis=='K':
        print(loetleFilmid(argument))
        return True
    elif tähis=='L':
        lisaFilm(nimi,žanr)        
        return True
    elif tähis=='V':
        kustutaFilm(argument)
        return True
    elif tähis=='E':
        return False
töötleKäsk(tähis,argument)
