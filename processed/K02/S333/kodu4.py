inglise_fail= input('sisesta inglisekeelse faili nimi: ')
eesti_fail= input('sisesta eestikeelse faili nimi: ')

f1= open(inglise_fail, "r")
#avab faili ja loeb teksti

f2= open(eesti_fail, "w")
f2.write (f1.read().replace('Hello','Tere'))
#kirjutab loetud teksti uude faili ja asendab sõnad

tekst= f1.read()
asendused= tekst.count ("Hello")
#loeb kokku kõik sõnad, mida ma asendada käskisin
#eraldi aknad toimib, aga terves programmis ei toimi enam :(

print('Programm tegi',asendused,'asendust tekstis')


f1.close()
f2.close()
#sulgeb failid, muidu jäävadki avatuks