#alustasin 28.11.2021
def väljasta_liin(eellane, jarglane, sonastik):
    if jarglane == eellane:
        print(jarglane)
        return True
    if jarglane in sonastik:
        isa = sonastik[jarglane][0]
        ema = sonastik[jarglane][1]
        toevaartus = väljasta_liin(eellane, isa, sonastik) or väljasta_liin(eellane, ema, sonastik)
        if toevaartus == True:
            print(jarglane)
        return toevaartus
    else: #kui ei ole kedagi puus
        return False