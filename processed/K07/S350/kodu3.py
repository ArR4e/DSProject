a=str(input("Isikukood "))
def sünnikuupäev(isikukood):
    sajand=int(a[0])
    if sajand<3:
        aasta="18"+a[1]+a[2]
    elif sajand <5 and sajand >2:
        aasta="19"+a[1]+a[2]
    elif sajand >4 and sajand <7:
        aasta="20"+a[1]+a[2]
    kuu=a[3]+a[4]
    if kuu==1:
        kuu="jaanuar"
    elif kuu==2:
        kuu="veebruar"
    elif kuu==3:
        kuu="märts"
    elif kuu==4:
        kuu="aprill"
    elif kuu==5:
        kuu="mai"
    elif kuu==6:
        kuu="juuni"
    elif kuu==7:
        kuu="juuli"
    elif kuu==8:
        kuu="august"
    elif kuu==9:
        kuu="september"
    elif kuu==10:
        kuu="oktoober"
    elif kuu==11:
        kuu="november"
    elif kuu==12:
        kuu="detsember"
    päev=a[5]+a[6]
    return(str(päev),". ",str(kuu), str(aasta))

print(sünnikuupäev(a))