f = open('taksohinnad.txt', encoding = 'UTF-8')
#Takso nimi, sisseistumise hind, kilomeetri hind

tee_pikkus = float(input('Sisestage teepikkus kilomeetrites: '))

taksode_hinnad = []
taksode_nimed = []
sisse_istumise_hinnad = []
kilomeetrite_hinnad = []
read = f.readlines()

if read != []:
    for rida in read:
        sõned = rida.split(',')
        for sõne in sõned:
            sõne = sõne.replace(',','').replace('\n', '')
            try:
                hinnad = float(sõne)
                taksode_hinnad.append(sõne)
            except:
                taksode_nimed.append(sõne)
                
    kilomeetrite_miinimum = taksode_hinnad[0]
    sisse_istumise_miinimum = taksode_hinnad[0]
    
    for i in range (len(taksode_hinnad)):
        if i %2:
            if taksode_hinnad[i] < kilomeetrite_miinimum:
                kilomeetrite_miinimum = taksode_hinnad[i]
            kilomeetrite_hinnad.append(taksode_hinnad[i])
        else:
            if taksode_hinnad[i] < sisse_istumise_miinimum:
                sisse_istumise_miinimum = taksode_hinnad[i]
            sisse_istumise_hinnad.append(taksode_hinnad[i])
            
    hinnad = []
    hind = 0
    
    for a in range (len(sisse_istumise_hinnad)):
        hind = float(sisse_istumise_hinnad[a]) + float(kilomeetrite_hinnad[a]) * tee_pikkus
        hinnad.append(hind)
        
    väikseim_hind = min(hinnad)
    indeks = hinnad.index(väikseim_hind)
    
    print('Kõige odavam on', taksode_nimed[indeks])
    
else:
    print('Fail on tühi')