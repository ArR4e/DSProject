with open(input('sisesta failinimi:')) as f:
    print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')

    bussid = []
    for line in f:
        line = line.strip().split()
        
        hours = int(line[1][:2]) - int(line[0][:2])
        minutes = int(line[1][3:]) - int(line[0][3:])
        if minutes < 0: hours -= 1
        difference = str(hours) + str(abs(minutes))
        if minutes == 0: difference += '0'
                    
        bussid.append(line + [difference])
        
    longest = 0
    mostExpensive = 0
    for buss in bussid:
        if int(buss[3]) > int(longest):
            longest = buss[3]
        if int(buss[2]) > mostExpensive:
            mostExpensive = int(buss[2])
    
    for buss in bussid:
        if buss[3] != longest and int(buss[2]) != mostExpensive:
            print(f'{buss[0]} {buss[1]} {buss[2]}')