def sünnikuupäev(isikukood):
    p2ev = 0
    kuu = 0
    aasta = 0
    sugu = 0
    #Saame järjendi igast numbrist, leiame, mitmendal kohal on järjendis vajalikud andmed ja määrame need antud muutujatele päev, kuu, aasta
    #Kuna isikukood koosneb tavalisel juhul 11 numbrist, siis tekib järjen [0,1,2,3,4,5,6,7,8,9,10], kus j2rjendi kohad 1,2 m2rgivad synniaastat
    #3,4 kuud ja 5,6 p2eva.
    for digit in isikukood:
        x = digit.split(" ")
        
        sugu = x[0]
        p2ev = x[5, 6]
        kuu = x[3, 4]
        aasta = x[1, 2]
        
        if sugu(0) == '3' or sugu(0) == '4':
            aasta = str(19) + aasta(1,2)
        if sugu(0) == '5' or sugu(0) == '6':
            aasta = str(20) + aasta (1, 2)
            
        if kuu (3, 4) == "01":
            kuu = 'jaanuar'
        elif kuu (3, 4) == "02":
            kuu = 'veebruar'
        elif kuu (3, 4) == "03":
            kuu = 'märts'
        elif kuu (3, 4) == "04":
            kuu = 'aprill'
        elif kuu (3, 4) == "05":
            kuu = 'mai'
        elif kuu (3, 4) == "06":
            kuu = 'juuni'
        elif kuu (3, 4) == "07":
            kuu = 'juuli'
        elif kuu (3, 4) == '08':
            kuu = 'august'
        elif kuu (3, 4) == '09':
            kuu = 'september'
        elif kuu (3, 4) == '10':
            kuu = 'oktoober'
        elif kuu (3, 4) == '11':
            kuu = 'november'
        elif kuu (3, 4) == '12':
            kuu = 'detsember'
            
            
        p2ev = x(5, 6)
        
        return(p2ev, kuu, aasta)
    #kuude jaoks tuleb meil eraldi teha andmebaas, mis saaks aru mis number vastab mis kuule ja liita kuu l6ppu tyhik (+ " ").
    
    #aastate puhul peame 2ra m22rama, kust maalt kirjutada ette 19 ja kust maalt 20. Selleks vaatame erinevatelt isikukoodidelt sugu, kui ees on
    #3 v 4, siis algab aasta 19.., kui sugu on 5 v 6, algab aasta 20..
    
    #p2eva saab lihtsalt sisestada arvuna ja selle jarele tuleb liita ". " koos tyhikuga
    
sünnikuupäev("50428149923")
print(sünnikuupäev("50428149923"))
#output XX. kuu aasta 