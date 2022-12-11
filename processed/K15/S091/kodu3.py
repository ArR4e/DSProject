fail = input('Sisesta failinimi: ')

jar = []
f = open(fail, 'r')
for rida in f:
    ennik = ((rida.strip().split(' ', 3)))
    jar.append(ennik)
   
for i in range(2):
    for buss in jar:
        for buss2 in jar:
            if buss != buss2:
                if buss[0]>buss2[0]:
                    if buss[1]<buss2[1]:
                        if int(buss[2])<int(buss2[2]):
                            jar.remove(buss2)
                        
jar.sort()
for el in jar:
    sone = el[0] + ' ' + el[1] + ' ' + el[2]
    print(sone)