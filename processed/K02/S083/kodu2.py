#Siis, kui hakkasin esmalt logifaile üleslaadima, märkasin, et mingil
#põhjusel oli minu Thonny seaded vahepeal resettinud ning programm
#ei loginud minu tegevusi. Lülitasin selle siis sisse ning kirjutasin oma
#kodutöö ümber. Tulevikus enam sellist viga ei tule.

pikkus = int(input('Sisestage elektriliini täisarvuline pikkus: '))
kaugus = int(input('Sisestage postide täisarvuline kaugus: '))
postide_arv = int(pikkus / kaugus) + 2

if kaugus == pikkus:
    print('Elektriliini jaoks on vaja vähemalt 2 posti!')
if kaugus == pikkus / 2:
    print('Elektriliini jaoks on vaja vähemalt ', int(postide_arv - 1), ' posti!')
else:
    print('Minimaalselt on elektriliini jaoks vaja ', int(postide_arv), ' posti!')
    