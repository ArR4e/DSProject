kasutaja = input("Sisesta kasutajanimi: ")
c = 0
f = open('users.txt','x')
while True:
    parool1 = input('Sisesta parool esimest korda: ')
    parool2 = input('Sisesta parool teist korda: ')
    if parool1 == parool2:
        if len(parool2)>= 8:
            if parool2.count('0') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('1') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('2') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('3') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('4') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('5') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('6') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('7') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('8') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            elif parool2.count('9') >= 1:
                parool2 = parool2[::-1]
                #f = open('users.txt','x')
                f.write(kasutaja+':'+parool2)
                f.close()
                break
            else:
                print('Parool ei sisalda numbreid')     
        else:
            print("Parool on lühem, kui 8 tähemärki")     
    else:
        print('Esimene parool ei kattu teisega')
    
    
    
