def sümbolite_sagedus(n):
    temp = {}
    for i in n:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    return temp

def erinevad_sümbolid(n):
    temp = set()
    for i in n:
        if i not in temp:
            temp.add(i)
    return temp

def grupeeri(n):
    th = 'aeiouõäöüAEIOUÕÄÜÖ'
    kh = 'hjlmnrsvkptgbdHJLMNRSVKPTGBDzZxXcCyYfFwWqQ'
    thl = set()
    khl = set()
    ehl = set()
    main = {}
    for i in set(n):
        if i in th:
            thl.add((i, n.count(i)))
        elif i in kh:
            khl.add((i, n.count(i)))
        else:
            ehl.add((i, n.count(i)))
    main["Täishäälikud"] = thl
    main["Kaashäälikud"] = khl 
    main["Muud"] = ehl
    return main