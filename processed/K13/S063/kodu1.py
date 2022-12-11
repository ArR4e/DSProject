'''-- Kodutöö nr. 13 - 1. Kasutatud auto hind rekursiivselt --'''
#################################################################
## funktsioon võtab sisse auto hinda ja aastate arvu ning tagastab
## auto hinda aastate pärast, iga aastaga auto hind kaotab 20%
def auto_hind(hind, aastad):
    if aastad == 0:
        return float(hind)
    else:
        return round(auto_hind(0.8*float(hind), aastad-1), 2)

print(auto_hind(8000.0, 5))