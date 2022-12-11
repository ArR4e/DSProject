def sünnikuupäev(Eesti_isikukood_sõnena):
    isikukood = list(Eesti_isikukood_sõnena)
    
    kuu = ''.join(isikukood[3:5])
    if kuu == '01':
        kuu_nimi = "jaanuar"
    elif kuu == '02':
        kuu_nimi = "veebruar"
    elif kuu == '03':
        kuu_nimi = "märts"
    elif kuu == '04':
        kuu_nimi = "aprill"
    elif kuu == '05':
        kuu_nimi = "mai"
    elif kuu == '06':
        kuu_nimi = "juuni"
    elif kuu == '07':
        kuu_nimi = "juuli"
    elif kuu == '08':
        kuu_nimi = "august"
    elif kuu == '09':
        kuu_nimi = "september"
    elif kuu == '10':
        kuu_nimi = "oktoober"
    elif kuu == '11':
        kuu_nimi = "november"
    elif kuu == '12':
        kuu_nimi = "detsember"

    päev_listis = isikukood[5:7]
    päev = ''.join(päev_listis)
     
     
    sünniaasta_listina = isikukood[1:3]
    sünniaasta = ''.join(sünniaasta_listina)
    
    sajand_listina = isikukood[0:1]
    sajand = ''.join(isikukood[0:1])
    if sajand == '1' or sajand == '2': #18. sajand
        sajandi_arv = "18"
    if sajand == '3' or sajand == '4': #19. sajand
        sajandi_arv = "19"
    if sajand == '5' or sajand == '6': #20. sajand
        sajandi_arv = "20"
        
    aastaarv = sajandi_arv + sünniaasta

   
    tagastus1 = päev + ". "+ kuu_nimi + " " + aastaarv

    return(tagastus1)

print(sünnikuupäev('60202190221'))