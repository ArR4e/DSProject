# Koosta argumentideta funktsioon bingo, mis genereerib bingonumbreid.
#Funktsioon peab järjendina tagastama 5 arvu, millest 3 on vahemikus 1 kuni 10 ning
#ülejäänud 2 on vahemikus 11 kuni 20.
#Funktsioon ei tohi lubada sellist olukorda, kus järjendisse jääksid korraga 1, 2 ja 3.
#Sellisel juhul tuleb genereerida uued arvud.
# Funktsioon peab olema ilma parameetritega ning tagastama 5 täisarvust koosneva järjendi
#sample(jär,<el.arv>) või sample(range(1,10),<el. arv>)

from random import sample

def bingo():
    
    esimene= list(range(1,11)) #teeme järjendi 1-10
    teine= list(range(11,21)) # teeme järjendi 11-20
    bingo1_3=[] #esimesed kolm numbrit
    bingo4_5=[] #viimased 2

#leiame kolm esimest arvu
    i=0 #abimuutuja tsüklite arvu loendamiseks
    n=0 #abimuutuja 1,2,3-reegli kehtestamiseks
    
    while i <3: #läbime tsüklit kolm korda
        arv=sample(esimene,1) #leiame juhusliku arvu ja salvestame järjendisse arv
        arv= arv[0] #järjendist toome arvu välja
        
        #arvude 1,2,3 korral tuleb kontrollida, ega neid juba pole
        if arv in range(1,4): 
           
            if n<1:#kui esimene arv selles vahemikus, siis välistame edasised
                n+=1
                pass #esimene kord läheb tsükkel lõpuni ja arv lisatakse
            else:
                continue #edaspidi minnakse algusesse ja genereeritakse uus arv
        elif arv in bingo1_3: #kui arv juba on järjendis, võtame uuesti
            continue
        
        #kui arv sobib, lisatakse järjendisse             
        i+=1 
        bingo1_3= bingo1_3+ [arv]

#leiame kaks viimast arvu
    i=0
    while i <2:
        arv=sample(teine,1)
        arv= arv[0]
        if arv in bingo4_5:
            continue #kui arv on juba olemas, genereerib uue
        i+=1
        bingo4_5= bingo4_5+ [arv]    
    
    return bingo1_3 + bingo4_5 #koostame 5 täisarvuga järjendi tulemuseks


