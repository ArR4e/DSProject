#Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse EU kinganumbrid
#ja kuvab ekraanile vastavad jalalaba pikkused sentimeetrites ümardatuna täisarvuks.
#Valem jalalaba pikkuse arvutamiseks on: pikkus = 2/3 * (kinganumber - 2).

#Faili nende ridade juures, kus arvuks teisendamine miskipärast ebaõnnestub,
#tuleb ekraanile kuvada „Vigane sisend” ning jätkata faili järgmise reaga

n= 1

f= open('kinganumbrid.txt')

while n==1:
    try:
        faili_sisu = f.readline()
        pikkus= round(2/3 *(float(faili_sisu)- 2))
        print(str(pikkus))
#kuni pole probleemi toodab programm vastuseid ja võtab uue rea, nagu readline() teeb
    except:
        if faili_sisu== '':
           break
           #kui jõuab viimase reani, paneb tsükli kinni
           #võib ka edasise käskluse anda
        else:
            print('Vigane sisend')
            n+= 1
            #annab veateate ja läheb n=2 tsüklisse
    while n==2:
        try:
            faili_sisu = f.readline()
            pikkus= round(2/3 *(float(faili_sisu)- 2))
            print(str(pikkus))
           
        except:
            if faili_sisu== '':
               break
                #kui jõuab viimase reani, paneb tsükli kinni
                #võib ka edasise käskluse anda
            else:    
                print('Vigane sisend')
                n-= 1
                #kui ei sobi rea sisu, annab veateate ja läheb esimesse tsüklisse tagasi
                #esimene tsükkel jätkab uuelt realt, et minna edasi
                # kui fail saab otsa kummaski tsüklis, paneb faili kinni
                #võib ka vajadusel midagi muud teha, hetkel midagi paremat pole võtta
            
