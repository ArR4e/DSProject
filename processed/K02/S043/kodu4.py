a = input("Olemasoleva faili nimi: ")
b = input("Uue faili nimi: ")
with open(a) as f:
    tekst = f.read()
    asendus = {'hello':'tere', 'Hello':'Tere'}
    luger = 0
    for src, target in asendus.items():
        luger += tekst.count(src)
        tekst = tekst.replace(src, target)

        with open(f'{b}.txt','w+' ) as f:
            f.write(tekst)
l = str(luger)
print("Tehti "+l+" asendust.")