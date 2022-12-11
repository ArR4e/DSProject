# Arvestame, et auto kaotab igal aastal väärtust 20% võrreldes eelmise aastaga.
# Kirjuta rekursiivne funktsioon (ehk funktsioon, mis kutsub välja iseennast),
# mis võtab sisse auto hinna ja aastate arvu ning tagastab, kui palju on auto väärt antud arvu aastate pärast.
# Funktsioon peab ümardama kõik tagastatavad hinnad kahe komakohani.
# >>> auto_hind(10000.0, 0)
# 10000.0
# >>> auto_hind(10000.0, 5)
# 3276.8
# >>> auto_hind(10000.0, 1)
# 8000.0
# >>> auto_hind(8000.0, 5)   # või auto_hind(10000.0, 6)
# 2621.44
# Seda ülesannet saab lahendada ka while-tsükliga või valemiga, aga lahendamine rekursiivse
# funktsiooniga aitab hästi mõista rekursiooni mõtet.

def auto_hind(hind, aastad):
    if aastad <= 0: # '==' töötab ainult juhul kui aastad on täisarvuline, aga nii ei pruugi olla. '<=' töötab ka komakohtadega
        return print(round(hind, 2))
    else:
        auto_hind(0.8*hind, aastad - 1)
auto_hind(1000,2.2)