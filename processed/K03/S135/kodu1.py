# Kirjuta programm, mis küsib kasutaja aastatulu (mittenegatiivne ujukomaarv) ja
# arvutab ning väljastab ekraanile maksuvaba tulu ümardatuna kahe kohani pärast koma.

# küsib kasutaja käest aastatulu kuni sisendiks on number
while True:
    try:
        aastatulu = float(input('sisesta enda aastatulu '))
        break
    except:
        print('see ei ole number, sisestage oma tulu uuesti')
    
maksuvabaTulu = 0

# aastatulu suuruse põhjal leiab maksuvaba tulu
if aastatulu > 0 and aastatulu <= 6000:
    maksuvabaTulu = aastatulu
elif aastatulu > 6000 and aastatulu <= 14400:
    maksuvabaTulu = 6000
elif aastatulu > 14000 and aastatulu <= 25200:
    maksuvabaTulu = 6000 - 6000 / 10800 * (aastatulu - 14400)


print('maksuvaba tulu on', round(maksuvabaTulu, 2), 'eurot')