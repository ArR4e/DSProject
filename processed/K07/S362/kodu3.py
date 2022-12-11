
def sünnikuupäev(sisend):
    a=list(sisend)
    if a[0]=='1' or a[0]=='2':
        aasta=int(a[1] + a[2])+1800
    elif a[0]=='3' or a[0]=='4':
        aasta=int(a[1] + a[2])+1900
    elif a[0]=='5' or a[0]=='6':
        aasta=int(a[1] + a[2])+2000
    
    kuupäev=a[5] + a[6]
    kuu_nr=a[3] + a[4]
    if kuu_nr=='01':
        kuu="jaanuar"
    elif kuu_nr=='02':
        kuu="veebruar"
    elif kuu_nr=='03':
        kuu="märts"
    elif kuu_nr=='04':
        kuu="aprill"
    elif kuu_nr=='05':
        kuu="mai"
    elif kuu_nr=='06':
        kuu="juuni"
    elif kuu_nr=='07':
        kuu="juuli"
    elif kuu_nr=='08':
        kuu="august"
    elif kuu_nr=='09':
        kuu="september"
    elif kuu_nr=='10':
        kuu="oktoober"
    elif kuu_nr=='11':
        kuu="november"
    elif kuu_nr=='12':
        kuu="detsember"
       
    sünnikuupäev="{0}. {1} {2}".format(kuupäev,kuu,aasta)
    sünnikuupäev2=' '.join([kuupäev+".", kuu, str(aasta)])
# 
#     print(aasta)
#     print(kuu_nr)
#     print(kuupäev)
#     print(kuu)
#     print(sünnikuupäev)
#     print(sünnikuupäev2)
    return sünnikuupäev




sisend='34503234215'


test=sünnikuupäev(sisend)
print(test)