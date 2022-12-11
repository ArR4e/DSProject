import film

print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===\n")


def töötleKäsk(indeks, argument):
    
    if indeks == 'K':
        
        while True:
            try:
                a = film.loetleFilmid(argument[1])
                break
            except:
                print("Sellest žanrist pole ühtegi filmi.")
                kask = input("Sisesta käsk: ")
                argument = kask.split()
                indeks = kask[0]

        str1 = ''
        for i in a:
            str1 += i
            str1 += '\n'
        print("Võimalikud filmid on: \n" + str1)
        
    if indeks == 'L':
        film.lisaFilm(" ".join(argument[2:]), argument[1])
        print("Film lisatud!")
        
    if indeks == 'V':
        film.kustutaFilm(argument[1])
        print("Film nimekirjast kustutatud!"+"\n"+"Head Vaatamist!")
        
    if indeks == 'E':
        return False
        
    
while True:
    kask = input("Sisesta käsk: ")
    argument = kask.split()
    indeks = kask[0]
    if indeks == 'E':
        break
    else:
        töötleKäsk(indeks, argument)