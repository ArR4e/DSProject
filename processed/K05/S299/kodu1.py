kasutajanimi= str(input('Sisestage oma kasutajanimi: '))

while True:
    parool= str(input('Sisestage oma parool: '))
    parool2= str(input('Sisestage parool uuesti: '))
    if parool == parool2 and len(parool) >= 8 and parool.isalpha() == False:
        f=open('users.txt','w')
        f.write(kasutajanimi + ':'+ parool[len(parool)::-1])
        f.close()
        break
    else:
        print('Parool ei sobi')
        
    

    
    
