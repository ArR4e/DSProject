def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    tagastatav_sõnastik = {}
    nimede_ja_isikukoodide_sõnastik = {}
    laste_maatriks = []
    nimede_maatriks = []
    
    f_lapsed = open(lastefailinimi, 'r', encoding='utf-8')
    f_nimed = open(nimedefailinimi, 'r', encoding='utf-8')
    
    laste_maatriks = [rida.strip().split() for rida in f_lapsed]
    nimede_maatriks = [rida.strip().split() for rida in f_nimed]
      
    for el in nimede_maatriks:
        el[1] = el[1] + ' ' + el[2]
        el.remove(el[2])
    #print(nimede_maatriks)
        
    for el in nimede_maatriks:
        nimede_ja_isikukoodide_sõnastik[el[0]] = el[1]
    #print(nimede_ja_isikukoodide_sõnastik)

    for i in range(len(laste_maatriks)):
        for j in range(len(laste_maatriks[i])):
             laste_maatriks[i][j] = nimede_ja_isikukoodide_sõnastik[laste_maatriks[i][j]]
    #print(laste_maatriks)
    
    for el in laste_maatriks:
        tagastatav_sõnastik[el[1]] = set()
        tagastatav_sõnastik[el[1]].add(el[0])
    #print(tagastatav_sõnastik)
    
    f_lapsed.close()
    f_nimed.close()
    
    return tagastatav_sõnastik