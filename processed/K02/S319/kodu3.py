import re

ees = input("Sisesta eesnimi: ").lower()
pere = input("Sisesta perenimi: ").lower()

kasutaja = (ees + '.' + pere).translate(str.maketrans({'õ':'o', 'ö':'o', 'ä':'a', 'ü':'u'}))

print(kasutaja)

