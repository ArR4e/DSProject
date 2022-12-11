import film

def töötleKäsk(käsu_tähis, käsu_args):
    if käsu_args == ' ' or käsu_args == '':
        return False
    if käsu_tähis == 'K':
        print(film.loetleFilmid(käsu_args))
        return True
    elif käsu_tähis == 'L':
        if käsu_args == []:
            return False
        
        film.lisaFilm(käsu_args[käsu_args.find(" ") + 1:], käsu_args[:käsu_args.find(" ")])
        print("Film lisatud!")
        return True
    elif käsu_tähis == 'V':
        film.kustutaFilm(käsu_args)
        print("Film kustutatud")
        return True
    else:
        return False
        
while True:
    käsk = input()

    if töötleKäsk(käsk[0], käsk[2:]) == False:
        print("Kas exit või ebaõige käsk")
        break