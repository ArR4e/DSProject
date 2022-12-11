sugupuu=[]
def väljasta_liin(eellane,järglane,sõnastik):
    for i in sõnastik:
        if eellane==järglane:
            sugupuu.append(järglane)
            eellane=''
            break
        if eellane in sõnastik[i]:
            sugupuu.append(eellane)
            eellane=i
            väljasta_liin(eellane,järglane,sõnastik)
            break
    if eellane!='':
        if sugupuu==[] or sugupuu[len(sugupuu)-1]!=järglane:
            return False
        elif sugupuu[len(sugupuu)-1]==eellane:
            for rida in sugupuu:
                print(rida)
            return True
sõnastik={'Urmas': ('Artur', 'Ülle'), 'Artur': ('Meelis', 'Ene'), 'Meelis': ('Siim', 'Niina'), 'Siim': ('Priit', 'Krõõt'), 'Ene': ('Oleg', 'Fatme'), 'Oleg': ('Vello', 'Liidia')}
väljasta_liin('Krõõt', 'Artur', sõnastik)