def sünnikuupäev(isikukood):
    isikukood= list(str(isikukood))#teeme sisendist järjendi, või lihtsalt võtame sõne indeksid
    
    päev= isikukood[5:7] #nendel postitsioonidel on päev
    päev= int(päev[0]+ päev[1]) #muudame järjendi sõneks või arvutuste puhul numbriks ka veel,kui vaja
    
    kuu= isikukood[3:5]
    if kuu[0]=='0':
        kuu= int(kuu[1])#juhul kui ühekohaline, siis võtame nulli ära
    elif kuu[0]=='1':
        kuu= int(kuu[0]+ kuu[1]) #see vaja arvuks teha, et indeksina kasutada
    kuu_sõnadega=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    kuu_sõnadega= kuu_sõnadega[(kuu-1)]
    
    #ära unusta, et peale 2000 aastat on ka inimesed sündinud!!!
    
    if int(isikukood[0])>4:#järjendi element tuleb teha arvuks, et saaks suurust võrrelda
        aastatuhat=20 #milleeniumi vahetusega on poiss 5 ja tüdruk 6 alguses, enne 3 ja 4
    elif int(isikukood[0])>=3:
        aastatuhat=19
    elif int(isikukood[0])<3:
        aastatuhat=18
    
    aasta= str(isikukood[1]+isikukood[2]) #kaks elementi üheks numbriks kokku
    #jätame aasta sõneks, et vajadusel null säiliks aastaarvu sees
    #võiks ka numbrina teha, aga siis lihtsalt mingi if-tingimus juurde, mis selle null paneb
    
    return('{0}. {1} {2}{3}'.format(päev, kuu_sõnadega, aastatuhat, aasta))
    
    #võiks veel lisada kontrolli, kas isikukood on õiges formaadis
    #ehk siis pikkus, päevade arv kuudes ja kuude arv aastates

#print(sünnikuupäev('50012314215'))