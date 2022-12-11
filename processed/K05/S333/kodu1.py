#veebilehe registreerimisvorm
#stringidega operaatorid
#https://realpython.com/python-strings/
numbrid=0
tähed=0


kasutajanimi= input('Sisesta kasutajanimi: ')

while True:
    parool1=input('Sisesta parool: ')
    parool2=input('Sisesta parool uuesti: ')
    pikkus= len(parool1)
    
    if parool1 != parool2:
        print('Teine sisestatud parool ei kattu esimesega!')
        continue
   
    elif pikkus < 8:
        print('Parool peab olema vähemalt 8 tähemärki pikk!')
        continue
    
    while pikkus> 0:
        for tähemärgid in parool1:

            if tähemärgid.isdigit():
                numbrid+=1
                pikkus-=1
                continue
            #kui leiab numbri, siis loendab selle ja arvestab parooli pikkuse
            #ühe võrra lühemaks
            elif tähemärgid.isalpha():
                tähed+=1
                pikkus-=1
                continue
            #sama asi,aga tähtedega
            #else:
                #print('Paroolis peab koosnema tähtedest ja numbritest!')
                #see osa pole vajalik, sest võib olla ka kirjavahemärke
                
            else: #juhul kui on mingi muu tähemärk,siis lihtsalt jätkab järgmisega
                pikkus-= 1
                continue
                
            break # väljub for tsüklist
        break# väljub teisest while tsüklist
    
    if numbrid== 0 and tähed== 0: #kui polnud tähti ega numbreid, siis läheb esimesse tsüklisse tagasi
        continue
        
    if numbrid <1: #numbriga saab määrata miinimumi ka
        print('Paroolis peab olema lisaks tähtedele ka number!')
        continue
    if tähed <1:
        print('Paroolis peab olema lisaks numbritele ka täht!')
        continue

    else:
        print('Parool sobib!')
        break

#Pöörame parooli tagurpidi
pikkus= len(parool1)
parool=''
while pikkus >0:
    parool= parool+ (parool1[pikkus-1])
#print parooli täht positsioonil pikkus-1,sest loendus algab nullist
#liidab sõnedena tähti tagurpidi ühte jorusse
    pikkus -=1 #tsükkel väheneb 
    
fail= open('users.txt', 'w')
fail.write(kasutajanimi+':')
fail.write(parool)
fail.close()
