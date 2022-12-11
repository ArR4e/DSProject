
def väljasta_liin(eellane, järglane, sugupuu):
    # oleme jõudnud liini pidi järglaseni,
    # tagasta True
    if eellane == järglane:
        print(eellane)
        return True
    else:
        järgmine = None
        # see tsükkel käib läbi kõik inimesed sugupuus
        # kui inimese vanem on eellase nimega, võta
        # see nimi järgmiseks
        for key in sugupuu.keys():
            if (sugupuu[key][0] == eellane) or (sugupuu[key][1] == eellane):
                järgmine = key
                break
        # järgmist inimest polnud sõnastikus, tagasta False
        if järgmine == None:
            return False
        # funktsiooni enda väljakutse, seekord otsi järgmise
        # inimese järglast
        #
        # kontroll on vajalik selleks, et mitte väljastada nimesid
        # kui liin puudub
        elif väljasta_liin(järgmine, järglane, sugupuu):
            print(eellane)
            return True
        # liini pole, tagasta False
        else:
            return False
