def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f1 = open(lapsed)
    f2 = open(nimed)
    koodid = []
    nimed = {}
    s = {}
    for rida in f1:
        koodidkoos = rida.strip().split(' ')
        ennik = (koodidkoos[0], koodidkoos[1])
        koodid.append(ennik)
    for rida in f2:
        nimedkoos = rida.strip().split(' ')
        nimed[nimedkoos[0]]= nimedkoos[1] + ' ' + nimedkoos[2]
    for vanem, laps in koodid:
        lapsenimi = nimed.get(laps)
        vanemanimi = nimed.get(vanem)
        vanemad = s.get(lapsenimi, set()) 
        vanemad.add(vanemanimi)
        s[lapsenimi] = vanemad
    
    return s
         
    
ss = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
vanemad = ''
for i in ss:
    vanemad_list = list(ss[i])
    vanemad = ', '.join(vanemad_list)
    print(i + ': ' + vanemad)