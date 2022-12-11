###############################################################################################################
## Failis taksohinnad.txt on kirjas taksode nimi, sisseistumise hind ja kilomeetri hind, eraldatult komadega. #
## Kirjuta programm, mis küsib kasutajalt tee pikkuse koju kilomeetrites ning väljastab vastavalt failis      #
## olevatele hindadele kõige odavama takso nime.                                                              #
###############################################################################################################

# küsime kasutajalt tee pikkust kilomeetrites    
tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding = "utf-8")
# hindade järjend
hinnad = []
# loendame failist ridade kaupa
for rida in f:
    # eemaldame liigseid tühikuid rea algusest ja lõpust
    # jagame rida sõnedeks koma järgi
    rida = rida.strip().split(",")
    takso_nimi = rida[0]
    sisse_hind = float(rida[1])
    km_hind = float(rida[2])
    
    # lisame hindade järjendi jooksev väärtuste paar
    hinnad += [[takso_nimi, sisse_hind + km_hind * tee_pikkus]]
f.close()

# juhul kui fail oli vigane või tühi, püüame vigu kinni
try:
    # esialgselt odavaim hind on kõige esimene hind järjendist
    # järjendi 'hinnad' esimese elemendi esimene element on takso nimi ja teine element on hind
    odavam_hind = hinnad[0][1]
    odavam_takso = hinnad[0][0]
    
    # jooksutame iga takso paari järgi
    for i in range(len(hinnad)):
        # kui jooksev hind on väiksem odavamaist, siis odavaim on praegu jooksev
        if float(hinnad[i][1]) < odavam_hind:
            odavam_hind = float(hinnad[i][1])
            odavam_takso = hinnad[i][0]
    
    # väljastame tulemust
    print("Kõige odavam on", odavam_takso+".")
except:
    # vastasel juhul väljastame, et ei saa leida
    print("Kõige odavamat taksot ei saa väljastada.")
###############################################################################################################