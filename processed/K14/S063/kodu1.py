'''-- Kodutöö nr. 14 - 1. Rekursiivne absoluutväärtus --'''
####################################################################################################
## Rekursiivne funktsioon võtab argumentideks järjendi, mille elementideks on arvud ja/või järjendid.
## Tagastab uue sama kujuga andmestruktuuri, kus kõik arvud on asendatud nende absoluutväärtusega.
def rek_abs(järjend):
    
    # tagastatav järjend, algselt tühi
    abs_järjend = []
    
    # kui antud järjend pole tühi
    if järjend:
        for el in järjend:
            # kui järjendi element on arv, siis lisa uue järjendi sisse
            if not isinstance(el, list):
                abs_järjend.append(abs(el))
            # kui see on omakorda järjend, siis tekita uus alamjärjend ja rakenda rekursiooni samm 
            else:
                abs_järjend.append(rek_abs(el))
    
    return abs_järjend
####################################################################################################
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
print([2, 6, [8, 12, 12, [4, [6], 3]], 7, [3.55, 3.55]])