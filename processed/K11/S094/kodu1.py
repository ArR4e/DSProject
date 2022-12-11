
def seosta_lapsed_ja_vanemad(lapsed_fail, nimed_fail):
     isikukoodid = {}
     # avame 2 faili korraga.
     with open(lapsed_fail) as isikukoodifail, open(nimed_fail) as nimedefail:
         # loeme läbi nimede faili sisu ja seostame igale isikukoodile
         # nime.
         for rida_andmed in nimedefail:
             # splittime ainult esimese tühiku, sest esimene on alati
             # isikukood ja teine nimi.
             rida_andmed_eraldatud = rida_andmed.split(' ', 1)
             
             # eemaldame newline
             rida_andmed_puhas = []
             for el in rida_andmed_eraldatud:
                 print(el)
             
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")