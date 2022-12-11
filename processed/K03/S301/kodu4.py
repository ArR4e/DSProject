f = open('kinganumbrid.txt', 'r', encoding='UTF-8')

while True:
    try:
        kinganumber = f.readline()
        if float(kinganumber) >= 0:
            
            print(round((float(kinganumber) - 2) *2/3))
        
    except:
        print('viga')
        





f.close()