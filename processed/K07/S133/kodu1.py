def poisse_ja_tüdrukuid(a):
    poisid=0
    eelviimane=""
    tüdrukud=0 
    for e in a:
        for character in e:
            if (character=="P" or character=="T") and eelviimane ==" ":
                if character == "T":
                    tüdrukud+=1
                    break
                elif character == "P":
                    poisid+=1
                    break
            else:
                eelviimane = character
    return (poisid,tüdrukud)
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))