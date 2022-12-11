def väljasta_liin(eellane, järglane, sõnastik, lõpp=[]):
    if lõpp == []:
        lõpp.append(järglane)
    if järglane in sõnastik.keys():
        järglased = sõnastik[järglane]
        if eellane in järglased:
            lõpp.append(eellane)
            lõpp.reverse()
            for üks in lõpp:
                print(üks)
            return True
        else:
            prindi = False
            for tulija in järglased:
                a = lõpp[::]
                a.append(tulija)
                if väljasta_liin(eellane, tulija, sõnastik, a):
                    return True
            return False
    else:
        return False