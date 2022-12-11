#filmide nimekiri
fail = open("filmid.txt.",'r')
filmid =[]
def loetleFilmid(žanr):
    while True:
        for rida in fail:
            if rida == "":
                break
            
            liik = (rida.strip().split(' - '))
            if liik == žanr:
                print(liik)
            
    fail.close()