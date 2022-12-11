f_lapsed = "lapsed.txt"
f_nimed = "nimed.txt"

def seosta_lapsed_ja_vanemad(file_lapsed, file_nimed):
    with open(file_lapsed, "r+", encoding='UTF-8') as f:
        sisu_lapsed = f.readlines()
    with open(file_nimed, "r+", encoding='UTF-8') as f:
        sisu_nimed = f.readlines()
    lapsed_vanemad = {}
    lapse_nimed = {}
    vanemate_nimed = {}
    for rida in sisu_lapsed:
        rida = rida.strip().split()
        lapse_id = rida[1]
        vanema_id = rida[0]
        for rida1 in sisu_nimed:
            rida1 = rida1.strip().split()
            if lapse_id in rida1:
                lapse_nimed[lapse_id] = rida1[1] + " " + rida1[2]
            if vanema_id in rida1:
                vanemate_nimed[vanema_id] = rida1[1] + " " + rida1[2]
    for rida in sisu_lapsed:
        rida = rida.strip().split()
        lapse_nimi = lapse_nimed[rida[1]]
        vanema_nimi = vanemate_nimed[rida[0]]
        if lapse_nimi not in lapsed_vanemad:
            lapsed_vanemad[lapse_nimi] = {vanema_nimi}
        if lapse_nimi in lapsed_vanemad:
            lapsed_vanemad[lapse_nimi].add(vanema_nimi)
    return lapsed_vanemad

lapsedjavanemad = seosta_lapsed_ja_vanemad(f_lapsed, f_nimed)

for laps in lapsedjavanemad:
    if len(lapsedjavanemad[laps]) == 2:
        print("{}: ".format(laps), end="")
        i = 0
        for vanem in lapsedjavanemad[laps]:
            if i < 1:
                i += 1
                print("{}, ".format(vanem), end="")
            else:
                print("{}".format(vanem), end="\n")

    else:
        for vanem in lapsedjavanemad[laps]:
            print("{}: {}".format(laps, vanem))