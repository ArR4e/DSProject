def sünnikuupäev(ik):
    a=int(ik[0])
    if a==1 or a==2:
        a=(1800+(int(ik[1])*10)+int(ik[2]))
    elif a==3 or a==4:
         a=(1900+(int(ik[1])*10)+int(ik[2]))
    elif a==5 or a==6:
        a=(2000+(int(ik[1])*10)+int(ik[2]))
    kuu=int(ik[3])
    if kuu==0:
        kuu=kuud[int(ik[4])-1]
    else:
        kuu=kuud[int(ik[4])+9]
    kp=int(ik[5])*10 + int(ik[6])
    return (str(kp) + ". " + kuu + " " +str(a))

kuud=["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
ik=str(input("Sisestage oma isikukood: "))
print(sünnikuupäev(ik))