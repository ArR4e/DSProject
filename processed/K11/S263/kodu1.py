# lastefailinimi = "lapsed.txt"
# nimedefailinimi = "nimed.txt"
def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    s = {}
    f_1 = open(lastefailinimi)
    for rida in f_1:
        lasteandmed = rida.strip().split(" ")
        vanema_isikukood = lasteandmed[0]
        lapse_isikukood = lasteandmed[1]
        lapsenimi = ""
        vanemad = ""
        f_2 = open(nimedefailinimi)
        for rida in f_2:
            nimedeandmed = rida.strip().split(" ", 1)
            isikukood = nimedeandmed[0]
            nimi = nimedeandmed[1]
            if vanema_isikukood == isikukood:
                vanemad = nimi
            elif lapse_isikukood == isikukood:
                lapsenimi = nimi

        s[lapsenimi] = s.get(lapsenimi, set())
        s[lapsenimi].add(vanemad)

        f_2.close()
    f_1.close()
    return s


print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
