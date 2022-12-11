nimed = []
def väljasta_liin(eellane, järglane, sõnastik):
    if eellane in sõnastik:
        nimed.append(eellane)
        return väljasta_liin(eellane, järglane, sõnastik) and True
    if järglane not in nimed:
        print('Pole') and False