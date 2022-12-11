lahtefail = input('Sisesta lähtefaili nimi koos .txt: ')
sihtfail = input('Sisesta sihtfaili nimi koos .txt: ')
# Abi võetud https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-string-in-python
lahtef = open(lahtefail) # Avab lähtefaili
sihtf = open(sihtfail, 'w') # Avab sihtfaili
loehello = lahtef.read() # Loeb lähtefaili
asendamisi = int(loehello.count('Hello')) # Uurib, kui palju sõnu peab asendama
tekst = loehello.replace('Hello', 'Tere') # Asendab sõnad Hello sõnaga Tere
# Abi võetud https://www.geeksforgeeks.org/python-copy-contents-of-one-file-to-another-file/
sihtf.write(tekst) # Kirjutab lähtefaili "tõlgitud" teksti
lahtef.close() # Sulgeb lähtefaili
sihtf.close() # Sulgeb sihtfaili
print(asendamisi)
