def väljasta_liin(eellane,järglane,sõnastik):
    def leia_liin(eellane,järglane,sõnastik):
        if eellane == järglane:
            return [järglane]
        if järglane in sõnastik:
            for vanem in sõnastik[järglane]:
                liin = leia_liin(eellane,vanem,sõnastik)
                if liin:
                    liin.append(järglane)
                    return liin
        else:
            return
    vastus = leia_liin(eellane,järglane,sõnastik)
    if vastus:
        print('\n'.join(vastus))
        return True
    else:
        return False