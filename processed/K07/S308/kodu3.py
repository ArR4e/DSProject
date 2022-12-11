isikukood='39910122345'
def sünnikuupäev(isikukood):
    päev=(isikukood[5]+isikukood[6])
    kuu=isikukood[3]+isikukood[4]
    ajastu=isikukood[0]
    if ajastu == '3' or ajastu == '4':
        aasta= '19'+isikukood[1]+isikukood[2]
    elif ajastu == '5' or ajastu == '6':
        aasta= '20'+isikukood[1]+isikukood[2]
    elif ajastu == '1' or ajastu == '2':
        aasta= '18'+isikukood[1]+isikukood[2]    
    if kuu == '01':
        kuu='jaanuar'
    elif kuu == '02':
        kuu = 'veebruar'
    elif kuu == '03':
        kuu='märts'
    elif kuu == '04':
        kuu='aprill'
    elif kuu == '05':
        kuu='mai'
    elif kuu == '06':
        kuu='juuni'
    elif kuu == '07':
        kuu='juuli'
    elif kuu == '08':
        kuu='august'
    elif kuu == '09':
        kuu='september'
    elif kuu == '10':
        kuu='oktoober'
    elif kuu == '11':
        kuu='november'
    elif kuu == '12':
        kuu='detsember'
    
    return(str(päev)+'. '+ str(kuu) + ' ' + str(aasta))    
               
print(sünnikuupäev(isikukood))