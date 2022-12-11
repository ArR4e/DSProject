#taksohinnad.txt
km = int(input('Sisestage kilometride arv: '))
f = open('taksohinnad.txt', encoding = 'UTF-8')
rida =[]

r1 = str(f.readline())
r11 = (r1.split(','))
try:
    km1 = float(r11[2])
    hp1 = float(r11[1])
    hind = hp1 + km * km1
    rida += [hind]
except:
        print('try again')

r2 = str(f.readline())
r22 = (r2.split(','))   
try:
    km2 = float(r22[2])
    hp2 = float(r22[1])
    hind = hp2 + km * km2
    rida += [hind]       
except:
        print('try again')

r3 = str(f.readline())
r33 = (r3.split(','))   
try:
    km3 = float(r33[2])
    hp3 = float(r33[1])
    hind = hp3 + km * km3
    rida += [hind]      
except:
        print('try again')
m = min(rida)
if rida[0] == m:
    print('Kõige odavam on ', str(r11[0]), '.')
if rida[1] == m:
    print('Kõige odavam on ', str(r22[0]), '.')
if rida[2] == m:
    print('Kõige odavam on ', str(r33[0]), '.')

f.close()