import film

def töötleKäsk(tahis, nimekiri):
    print(film.loetleFilmid('multikas'))
    

f = open('filmid2.txt')
x = []
for a in f:
    x.append(a.strip())
töötleKäsk('K', 'filmid.txt')