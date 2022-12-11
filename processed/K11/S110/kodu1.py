def seosta_lapsed_ja_vanemad(f_lapsed, f_vanemad):
    sõnastik = {}
    f_lapsed = open(f_lapsed)
    lapsed = {}
    vanemad = {}
    f_vanemad = open(f_vanemad)
    
    for rida in f_lapsed:
        vanem, laps = rida.strip('\n').split(' ')
        sõnastik[vanem] = laps
#         if vanem in f_vanemad:
#             vanem = 
    for nimi in f_vanemad:
        nimi = nimi.strip('\n').split(' ')

    f_vanemad.close()
    #sõnastik[vanemad] = lapsed
    f_lapsed.close()
    return sõnastik
    
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
