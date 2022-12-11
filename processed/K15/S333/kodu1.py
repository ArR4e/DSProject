#sobivad vaid red, kus TÜ veeebiaadress
# http://www.ut.ee/
#prindime kasutajanimed

#toome mooduli regulaaravaldisele
import re 

#avame faili
f=open('aadressid.txt', encoding= 'UTF-8')

for rida in f:
    if re.match('(http://www.ut.ee/~)',rida): #loeme ainult sobiva veebilehega ridu
        sõnad= rida.split('/') #kaldkriips on eraldajaks , teeme selle abil järjendi
        print(sõnad[3].lstrip('~')) #teame, mis kohal peaks oelma kasutajanimi ja prindime
f.close()