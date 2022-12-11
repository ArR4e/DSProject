def loetleFilmid( märul ):
   f = open('filmid.txt',mode='a+', encoding = 'UTF-8')
   g = []
   while True:
        a = (f.readline().strip())
        if a == '':
           break
        b = a.split( ' - ')
        if b[1] == märul:
            g= g+([b[0]])
   f.close()
   return g
#print(loetleFilmid('märul'))

def lisaFilm(kevade, märul):
    f = open('filmid.txt',mode='a+', encoding = 'UTF-8')
    while True:
        a = (f.readline().strip())
        if a == '':
           f.write("\n"+str(keavde) + ' - ' + str(märul))
           break
    f.close()

def kustutaFilm(kevade):
    f = open('filmid.txt',mode='a+', encoding = 'UTF-8')
    while True:
        a = (f.readline().strip())
        if a == '':
           break
        elif kevade in a:
            del a
        f.close()
            
   