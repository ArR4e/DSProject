
def rek_abs(järjend1):
    järjend2 = []                         # Siia järjendisse kirjutama abs väärtused
    for i in järjend1:                    # elementhaaval käime jörjendi läbi
        if isinstance(i, list):           # kontrollime kas list on listi sees.
            järjend2.append(rek_abs(i))   # Seejärel käime alamlisti läbi võttes ka sealsete elementide abs väärtused.
        else:                             
            järjend2.append(abs(i))       # Tavalise listi puhul me lihtsal anname elemendile abs väärtuse ja appendime selle järjendisse
    return järjend2

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))