def seosta_lapsed_ja_vanemad(fail1, fail2):
    sõnastik = {}
    f= open(fail1)
    for rida in f:
        vanemad = set()
        vanemad = []
        korrastatud = rida.split()
        vanem = korrastatud[0]
        laps = korrastatud[-1]
        
        f2=open(fail2)
        for rida in f2:
            korrastatud2= rida.split()
            kood = korrastatud2[0]
            nimi_järjend = korrastatud2[1:]
            nimi = (" ".join(map(str,nimi_järjend)))
            
            if laps == kood:
                lapsenimi = nimi
                vanemad = set()
                #leian lapsele kõik teadalolevad vanemad

                with open(fail1) as f:
                    for rida in f:
                        
                        korrastatud3 = rida.split()
                        vanem3 = korrastatud3[0]
                        if korrastatud3[-1] ==laps:

                            with open(fail2) as f:
                                for rida in f:
                                    korrastatud4 = rida.split()
                                    
                                    if korrastatud4[0] == vanem3:
                                        vanemanimi = korrastatud4[1:]
                                        vanemanimi_korrastatud = (" ".join(map(str,vanemanimi)))
                                        vanemad.add(vanemanimi_korrastatud)
                                        
                        else:
                            continue
                                    
                                    
                                    
            
            else:
                continue
            

        sõnastik[lapsenimi]=vanemad
    f.close()
    f2.close()
    return sõnastik

#print(sõnastik)
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))