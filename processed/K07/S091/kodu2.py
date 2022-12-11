f = open('taksohinnad.txt', 'r', encoding="utf-8")
tee = float(input("Sisesta tee pikkus kilomeetrites: "))
odav = 1000000
odavNimi = ''
while True:
    a = f.readline().strip()
    if a == "":
        break
    b = a.split(',')
    nimi = b[0]
    hind = float(b[1])
    kmHind = float(b[2])
    summa = hind + kmHind*tee
    if summa < odav:
        odav = summa
        odavNimi = nimi

print(f'Kõige odavam on {odavNimi}.')