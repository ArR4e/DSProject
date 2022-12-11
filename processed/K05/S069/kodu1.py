fail = open('users.txt', 'a+')

nimi = input('Sisestage kasutajanimi: ')
parool = input('Sisestage parool: ')
parool2 = input('Sisestage parool uuesti: ')

parool_list = list(parool)
parool2_list = list(parool2)
i = []
if parool_list == parool2_list:
    if len(parool_list) >= 8:
        for sõne in parool_list:
            try:
                i = i + [int(sõne)]
            except:
                continue
        if len(i) > 0:
            parool_list.reverse()
            sõne = ''.join(parool_list)
            fail.write(nimi+':'+sõne+'\n')
        else:
            print('Parool peab sisaldama numbreid ja tähti')
    else:
        print('Liiga lühike parool')
else:
    print('Ei sisestatud sama parooli!')
    

    
fail.close()