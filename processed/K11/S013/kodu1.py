def seosta_lapsed_ja_vanemad(x,y):
    lapsed = open(x)
    nimed = open(y) 
    sõnastik1 = {}
    sõnastik2 = {}
    for rida in nimed:
        rida = rida.strip("\n")
        rida = rida.split(" ", 1)
        sõnastik1[rida[0]] = rida[1]
    for rida in lapsed:
        rida = rida.strip("\n")
        rida = rida.split(" ")
        lapsenimi = sõnastik1[rida[1]]
        vanemanimi = sõnastik1[rida[0]]
        if lapsenimi in sõnastik2:
            sõnastik2[lapsenimi].add(vanemanimi)
            
        else:
            sõnastik2[lapsenimi] = set()
            sõnastik2[lapsenimi].add(vanemanimi)
        

    return sõnastik2


print(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))