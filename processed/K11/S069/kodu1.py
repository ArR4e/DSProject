sõnastik={}
teinesõnastik={}
vastus={}
def seosta_lapsed_ja_vanemad(fail_lapsed, fail_nimed):
    lapsed = open(fail_lapsed)
    nimed = open(fail_nimed)
    for line in nimed:
        järjend = []
        array = line.split()
        key = array.pop(0)
        hulk = set()
        for el in array:
            järjend += [el]
        sõnastik[key]=järjend
    for line in lapsed:
        järjend = []
        array = line.split()
        try:
            i=' '.join(teinesõnastik[array[1]])
            järjend += [i]
            järjend += [array[0]]
            teinesõnastik[array[1]]= järjend
        except:
            järjend += [array[0]]
            teinesõnastik[array[1]]=järjend
    lapsed = open(fail_lapsed)
    for line in lapsed:
        hulk=set()
        array = line.split()
        laps = ' '.join(sõnastik[array[1]])
        vanemadHulk = teinesõnastik[array[1]]
        for nimi in vanemadHulk:
            i = ' '.join(sõnastik[nimi])
            hulk.add(i)
        vastus[laps]=hulk
    return vastus

seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')


for el in vastus:
    järjend = []
    for nimed in vastus[el]:
        järjend += [nimed]
    try:
        print(el+': '+järjend[0]+', '+järjend[1])
    except:
        print(el+': '+järjend[0])
            
        