### Kasutajalt küsitav teepikkus
teepikkus = float(input('Kui pikk on teie teekond kilomeetrites?'))

### Vajalikud järjendid
taksonimed = []
sõiduhinnad = []

### Funktsioon, mis leiab kahe eelneva järjendi abil madalama hinnaga takso nime
def madalam_hind():
    madalam = min(sõiduhinnad)
    indeks = sõiduhinnad.index(madalam)
    return taksonimed[indeks]
    

### Põhiprogramm
h1 = open('taksohinnad.txt')

for line in h1:
    hinnad = line.split(",") # 
    taksonimed.append(hinnad[0]) # Lisan taksode nimed järjendisse
    sissehind = float(hinnad[1].strip()) # Sisseastumishind iga takso kohta
    kmhind = float(hinnad[2].strip()) # Kilomeetri hind iga takso kohta
    sõiduhinnad.append(sissehind + kmhind*teepikkus) # Arvutan ja lisan sõidu täishinnad järjendisse


print('Kõige odavam on', madalam_hind())

    
    