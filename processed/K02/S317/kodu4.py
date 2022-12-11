with open("MAEITEA.txt", "r") as fail :
    tekst = fail.read()
tekst = tekst.replace('tere', 'tsau')
print(tekst)
with open('MAEITEA2.txt', 'w') as fail:
    fail.write(tekst)
print(tekst.count('tsau'))