fail = open('kinganumbrid.txt', encoding = 'utf-8')

while True:
    try:
         
         kinganumber = fail.readline()
         if kinganumber == '':
             break
         jalalaba_pikkus = 2/3 * (float(kinganumber) - 2)
         print(round(jalalaba_pikkus))
         
         
    except:
        
        print('Vigane sisend')
        

fail.close()
