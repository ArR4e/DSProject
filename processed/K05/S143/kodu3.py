a = 0
def moos(s,v,k):
    return(int(k/5) if (s!=0 and k%5==0 and v<k and v!=0 and k/5<=s) else (-1 if k>(s*5+v*1) else (s+v if k==(s*5+v*1) else ((lambda x: lambda y,z,w,q: x(x,y,z,w,q))(lambda s,L,S,W,I: I+W if (W<5 and S>=W) else (-1 if (W<5 and W>S) else (-1 if (W > 1 and S == 0) else (s(s,L-1,S,W-5,I+1) if (L>0 and W>=5) else (s(s,L,S-1,W-1,I+1))))))(s,v,k,a)))))
print(moos(1,3,4))
    
#Disclaimer:
#Nii jah ma tean et küsiti koodi loetavust, aga ma tahtsin ennast proovile panna kasutades järjekordset rekursiivset lambdafunktsiooni
#
#Anyway, et kood oleks loetavam, (mida ta ei ole väga, kasutan ma kommentaare et natukenegi seletada mis toimub)
#esiteks, funktsioon moos võtab argumentideks s (*S*uurte karpide arv), v (*V*äikeste karpide arv), k (moosi *K*ogus kilogrammides) ja a (kasutatud karpide *A*rv)
#seejärel, esimene edge case mida funktsioon uurib on siis kui k jagub s-ga ja s ei ole 0, sest ma ei viitsinud seda kuskile mujale vahele pressida.
#siis, teeb ta teiste edge casede kontrollid: kui k on suurem kui kõikidesse karpidesse kokku moosi mahub, väljastab funktsioon -1
#kui kõik karbid kuluvad täpselt ära moosi tegemiseks, väljastab funktsioon suurte ja väikeste karpide arvude summa
#ning viimaks, kui miski nendest tingimustest pole täidetud, asub funktsioon täitma rekursiivset lambdafunktsiooni
#esiteks ma defineerin ära (lambda x: lambda y,z,w,q: x(x,y,z,w,q)), mis defineerib ära funktsiooni rekursiivsuse
#sisendiks võtab see funktsioon funktsiooni ja see funktsioon defineerib järgmise funktsiooni, mis võtab sisendiks 4 arvu (s,v,k,a) ning
#funktsiooni enda
#seejärel, ma defineerin esimese funktsiooni sisendi, milleks on lambdafunktsioon, mis on minu põhialgoritm.
#see lambdafunktsioon võtab sisendiks funktsiooni enda ning neli argumenti, milleks on L (kui suured (*L*arge) moosikarbid),
#S (väiksed (*S*mall) moosikarbid), M (moosi kaal(*W*eight) kilogrammides) ning I (kasutatud karpide arv (*I*nteger))
#see funktsioon hakkab järjest läbi lahendama ülesannet. Kui moosi on vähem kui 5 kg ja väikseid karpe on piisavalt, väljastatakse moosi kogus
#Kui moosi on rohkem kui 0 kg, aga nii väikesed kui ka suured karbid on otsas, siis väljastatakse -1
#Kui suurte karpide arv on suurem kui 0 ja moosi on rohkem kui 5 kg, siis rakendatakse funktsiooni argumentidega L-1,S,W-5 ja I+1
#Kõigil muudel juhtudel rakendatakse funktsiooni argumentidega L,S-1,W-1 ja I+1
