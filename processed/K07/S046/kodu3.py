def sünnikuupäev(a):
    aastad = {'1':'18','2':'18','3':'19','4':'19','5':'20','6':'20'}
    kuud = {    '01':'jaanuar','02':'veebruar','03':'märts','04':'aprill','05':'mai','06':'juuni','07':'juuli','08':'august','09':'september','10':'oktoober','11':'november','12':'detsember'}
    sajand = aastad[a[0]]
    sünniaasta = a[1:3]
    sünnikuu = kuud[a[3:5]]
    sünnipäev = a[5:7]
    return(sünnipäev+". "+sünnikuu+" "+sajand+sünniaasta)
    
print(sünnikuupäev('50206112789'))