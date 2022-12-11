from string import punctuation
from random import randint
def suurväike(sisendsõne):
    kirjavahemargid = punctuation
    votab_suvalise_kirjavahemargi_leidmiseks_suvalise_arvu_0_st_kirjavahemarkide_arvuni = randint(0,len(kirjavahemargid))
    suvalinekirjavahemark = punctuation[votab_suvalise_kirjavahemargi_leidmiseks_suvalise_arvu_0_st_kirjavahemarkide_arvuni]
    list_millest_hiljem_saab_vajalik_sone = []
    for taht in list(sisendsõne):
        if taht.islower():
            suurtaht = taht.upper()
            list_millest_hiljem_saab_vajalik_sone.append(suurtaht)
        elif taht.isupper():
            vaiketaht = taht.lower()
            list_millest_hiljem_saab_vajalik_sone.append(vaiketaht)
        elif taht == " ":
            tyhik = " "
            list_millest_hiljem_saab_vajalik_sone.append(tyhik)
        else:
            list_millest_hiljem_saab_vajalik_sone.append(suvalinekirjavahemark)
    viimane_sone_mis_välja_prinditakse = "".join(list_millest_hiljem_saab_vajalik_sone)
    return(viimane_sone_mis_välja_prinditakse)
print(suurväike('Michael Andreas Barclay de Tolly'))