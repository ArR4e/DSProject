#Taksohinnad
andmed = []
hinnad = []

f = open('taksohinnad.txt', encoding='UTF-8')
for rida in f:
    andmed.append(list(rida.strip().split(',')))
    andmed[-1][-1] = float(andmed[-1][-1])
    andmed[-1][-2] = float(andmed[-1][-2])
f.close()

koduni = float(input('Sisesta tee pikkus kilomeetrites: '))

for firma in andmed:
    hinnad.append(firma[1] + firma[2] * koduni)

try:
    print('Kõige odavam on ', andmed[hinnad.index(min(hinnad))][0])
except ValueError:
    print('Viga! Kas sa oled ikka kindel, et faili on taksohinnad sisestatud ja kodutee pikkus on korrektne?')
    