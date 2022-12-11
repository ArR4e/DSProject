def erinevad_sümbolid(sone):
    temp = set([])
    for el in sone:
        if el in temp:
            continue
        else:
            temp.add(el)
    return temp

def sümbolite_sagedus(sone):
    temp = {}
    for el in sone:
        if el in temp:
            temp[el] += 1
        else:
            temp[el] = 1
    return temp

def grupeeri(sone):
    taishaalikud = ['a','e','i','o','u','õ','ä','ö','ü']
    kaashaalikud = ['b','d','g','p','t','k','c','f','h','j','l','m','n','q','r','s','v','w','x','y','z']

    for i in range(len(taishaalikud)):
        temp = taishaalikud[i].upper()
        taishaalikud.append(temp)
    for i in range(len(kaashaalikud)):
        temp = kaashaalikud[i].upper()
        kaashaalikud.append(temp)
    muud = [' ','.','"',"'",'?','!','-',',']
    temp = {'Täishäälikud': {}, 'Kaashäälikud': {}, 'Muud': {}}
    #taishaalikud
    temp_set = set()
    for el in taishaalikud:
        taht = el
        count = 0
        if not el in sone:
            continue
        else:
            for letter in sone:
                if letter == el:
                    count += 1
        temp_set2 = (taht, count)
        temp_set.add(temp_set2)
    print(temp_set)
    temp['Täishäälikud'] = temp_set
    
    #kaashaalikud
    temp_set = set()
    for el in kaashaalikud:
        taht = el
        count = 0
        if not el in sone:
            continue
        else:
            for letter in sone:
                if letter == el:
                    count += 1
        temp_set2 = (taht, count)
        temp_set.add(temp_set2)
    print(temp_set)
    temp['Kaashäälikud'] = temp_set
    
    #muud
    temp_set = set()
    for el in muud:
        taht = el
        count = 0
        if not el in sone:
            continue
        else:
            for letter in sone:
                if letter == el:
                    count += 1
        temp_set2 = (taht, count)
        temp_set.add(temp_set2)
    print(temp_set)
    temp['Muud'] = temp_set
                
    return temp


