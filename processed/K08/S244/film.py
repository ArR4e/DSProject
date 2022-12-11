def loetleFilmid(žanr):
    list1 = []
    fail = open('filmid.txt', encoding ="UTF-8")
    for x in fail:
        nimi = x.strip()
        järjend = list(nimi.split(' - '))

        if žanr in järjend:
            list1.append(järjend[0])
    fail.close()
    return list1
        
def lisaFilm(žanr, nimi):    
    fail = open('filmid.txt', 'a', encoding ="UTF-8")
    fail.writelines('\n' + žanr + ' - ' + nimi)
    fail.close()

def kustutaFilm(nimi):
    andmed = ''
    fail = open('filmid.txt', 'r', encoding ="UTF-8")
    for rida in fail:
        x = rida.strip()
        järjend = list(x.split(' - '))
        if järjend[0] == nimi:
            rida.replace(nimi, "")
        else:
            andmed += rida
            
            
    fail.close
    fail = open('filmid.txt', 'w', encoding ="UTF-8")
    fail.write(andmed)
    fail.close()
        
nimi = input('Sisesta filminimi: ')
žanr = input('Sisesta žanri nimi: ')