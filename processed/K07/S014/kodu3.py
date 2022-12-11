isikukood=''

# ## kui tegin sellise funktsiooni, siis.....(vt allpool)
# def kuu_sõnadega(kuu):
#     if kuu=='01':
#         kuu='jaanuar'
#     elif kuu=='02':
#         kuu='veebruar'
#     elif kuu=='03':
#         kuu='märts'
#     elif kuu=='04':
#         kuu='aprill'
#     elif kuu=='05':
#         kuu='mai'
#     elif kuu=='06':
#         kuu='juuni'
#     elif kuu=='07':
#         kuu='juuli'
#     elif kuu=='08':
#         kuu='august'
#     elif kuu=='09':
#         kuu='september'
#     elif kuu=='10':
#         kuu='oktoober'
#     elif kuu=='11':
#         kuu='november'
#     elif kuu=='12':
#         kuu='detsember'
        
def sünnikuupäev(isikukood):
    isikukood=list(isikukood)
    aasta_algus=''
    if isikukood[0]=='1' or isikukood[0]=='2':
        aasta_algus='18'
    elif isikukood[0]=='3' or isikukood[0]=='4':
        aasta_algus='19'
    elif isikukood[0]=='5' or isikukood[0]=='6':
        aasta_algus='20'
    
    aasta=isikukood[1:3]
    aasta=''.join(aasta)
    aasta=''.join([aasta_algus,aasta])
        
    kuu=isikukood[3:5]
#     kuu_teisendamiseks=''.join(kuu) ##SEE SIIN millegipärast ei tööta
#     kuu=kuu_sõnadega(kuu_teisendamiseks)##miks on väärtus None?
    kuu=''.join(kuu)
    if kuu=='01':
        kuu='jaanuar'
    elif kuu=='02':
        kuu='veebruar'
    elif kuu=='03':
        kuu='märts'
    elif kuu=='04':
        kuu='aprill'
    elif kuu=='05':
        kuu='mai'
    elif kuu=='06':
        kuu='juuni'
    elif kuu=='07':
        kuu='juuli'
    elif kuu=='08':
        kuu='august'
    elif kuu=='09':
        kuu='september'
    elif kuu=='10':
        kuu='oktoober'
    elif kuu=='11':
        kuu='november'
    elif kuu=='12':
        kuu='detsember'

    kuupäev=isikukood[5:7]
    kuupäev=''.join(kuupäev)
    kuupäev=kuupäev+'.'
    
    sünniaeg=' '.join([kuupäev,kuu,aasta])

    return sünniaeg

print(sünnikuupäev('39910122345'))
    