def rek_abs(jrnd):
    if jrnd == []:
        # tagasta tühi järjend kui see on tühi
        return []
    else:
        # kui esimene element on järjend,
        # käi see omakorda läbi rekursiivselt
        if isinstance(jrnd[0], list):
            return [rek_abs(jrnd[0])] + rek_abs(jrnd[1:])
        else:
            # kui esimene element ei ole järjend,
            # leia absoluutväärtus ja konstrueeri
            # uus järjend
            
            # käi läbi ülejäänud elemendid sama funktsiooniga
            if jrnd[0] > 0:
                return [jrnd[0]] + rek_abs(jrnd[1:])
            else:
                return [-jrnd[0]] + rek_abs(jrnd[1:])
