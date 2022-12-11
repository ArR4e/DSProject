#väljastab tulumaksu vaba tulu sisendi põhjal

#while True:
#hoiab programmi tsüklis, et mugavam testida oleks


tulu= float(input('Sisesta oma aastatulu '))

valem= 6000- 6000/ 10800* (tulu - 14400)
   # if tulu == 0:
    #    print('programm lõpetatud!')
     #   break
    
if tulu <=0 :
    print('Sisesta positiivne arv!')
else:

    if tulu < 6000 :
        print('Maksuvaba tulu on '+ str(tulu) + ' eurot.')
         
    elif tulu >= 6000 and tulu < 14400:
        print('Maksuvaba tulu on '+ '6000' + ' eurot.')
    # and, mitte or, sest mõlemad tingimused peavad kehtima

    elif tulu >= 14400 and tulu < 25200:
        print('Maksuvaba tulu on '+ str(round(valem, 2)) + ' eurot.')

    elif tulu >= 25200 :
        print('Maksuvaba tulu on '+ '0' + ' eurot.')
            
   # print('\n'+'Väljumiseks sisesta 0'+'\n')
    #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
'''
automaatkontrollile ei meeldinud minu while tsükkel,
millega ma hoidsin programmi töös, et saaks järjepanu sisendeid kontrollida
kasutaja sai programmist väljuda sisendiga "0". automaatkontroll seda ei osanud
kommenteerisin selle välja, aga ta tegelikult peaks töötama.

'''