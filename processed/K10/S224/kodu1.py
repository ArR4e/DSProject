def erinevad_sümbolid(sõne):
    sõne = set(sõne)
    return sõne


def sümbolite_sagedus(sisend):
    d = {}
    
    for el in sisend:
        if el in d:
            d[el] = d[el] + 1
        else:
            d[el] = 1
    
    return d


def grupeeri(sõna):
    häälikud = {"täishäälikud": [],
                "kaashäälikud": [],
                "muud" : []
                }
    
    täishäälikud= "aeiouõäöü"
    kaashäälikud = "bdfghjklmnprsztv"
    sagedus = sümbolite_sagedus(sõna)

    for täht in sagedus:
        if täht in täishäälikud:
            häälikud["täishäälikud"].append((täht, sagedus[täht]))
        elif täht in kaashäälikud:
            häälikud["kaashäälikud"].append((täht, sagedus[täht]))
        else:
            häälikud["muud"].append((täht, sagedus[täht]))
    
    for võti in häälikud:
        häälikud[võti] = set(häälikud[võti])
            
    return häälikud


            

            
        

    

