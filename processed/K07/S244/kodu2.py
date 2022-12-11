
teekond = float(input('Sisesta tee pikkus kilomeetrites: '))

fail = open('taksohinnad.txt', encoding="UTF-8")
takso1 = fail.readline().strip()
järjend1 = list(takso1.split(','))
if järjend1 != ['']:
    tulemus1 = float(järjend1[1]) + float(teekond) * float(järjend1[2])

takso2 = fail.readline().strip()
järjend2 = list(takso2.split(','))
if järjend1 != ['']:
    tulemus2 = float(järjend2[1]) + float(teekond) * float(järjend2[2])

takso3 = fail.readline().strip()
järjend3 = list(takso3.split(','))
if järjend1 != ['']:
    tulemus3 = float(järjend3[1]) + float(teekond) * float(järjend3[2])
fail.close()
if järjend1 != [''] and järjend2 != [''] and järjend3 != ['']:
    if tulemus3 < tulemus2 and tulemus3 < tulemus1:
        print('Kõige odavam on ' + järjend3[0] + '.')
    
    elif tulemus2 < tulemus1 and tulemus2 < tulemus3:
        print('Kõige odavam on ' + järjend2[0] + '.')

    else:
        print('Kõige odavam on ' + järjend1[0] + '.')



    







