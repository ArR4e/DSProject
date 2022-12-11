def seosta_lapsed_ja_vanemad(laste_fail,nimede_fail):
    laste=open(laste_fail,encoding="UTF-8")
    lapsed_ees={}   #teen kaks eraldi sõnastiku, ühes on ees lapse isikukood, teises vanema
    lapsed_järgi={}
    for i in laste:
        rida=i.strip().split()
        lapsed_ees[rida[1]]=rida[0]
        lapsed_järgi[rida[0]]=rida[1]
    laste.close()
    nimede=open(nimede_fail)
    nimed={}
    for i in nimede:
        rida=i.strip().split()
        while len(rida)>2:
            rida[1]+=" "+str(rida.pop(2))
        nimed[rida[0]]=rida[1]
    nimede.close()
    for i in lapsed_ees:
        väljund={}
        if i not in nimed:
            pass
        else:
            lapse_nimi=nimed[i]
            print(i)
            vanemad=()
            for j in lapsed_järgi:
                if i==lapsed_järgi[j]:
                    vanema_nimi=nimed[j]
                    vanemad+=(vanema_nimi,)
            väljund[lapse_nimi]=set(vanemad) #Siin tekkis probleem :( Marial poleks nagu vanemaid
            print(vanemad)
            print(väljund)
seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
