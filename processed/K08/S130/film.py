
def loetleFilmid(žanr):
    f = open('filmid.txt', encoding = 'utf-8')
    onneed = []
    for filmid in f:
        A = filmid.strip().split(' - ')
        nimi = A[0]
        if A[1] == žanr:
            onneed.append(nimi)
    return onneed
    f.close()

def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding = 'utf-8')
    f.write('\n' + nimi + ' - ' + žanr + '\n') 
    f.close()
    
def kustutaFilm(nimi):
    f = open('filmid.txt', 'r', encoding = 'UTF-8')
    Uus = []
    for filmid in f:
        A = filmid.strip().split(' - ')
        if nimi not in A:
            Uus.append(A[0:2])
    print(Uus)
    f.close()
    f = open('filmid.txt', 'w',  encoding = 'UTF-8')
    for element in Uus:
        f.write((str(element[0]) + ' - ' + str(element[1]) ) + '\n')
    f.close()