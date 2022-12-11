import random

def suurväike(sona):
    uussona = ""
    kirjamark = (list(kirjavahemargid))[random.randint(0, int(len(kirjavahemargid)-1))]
    for i in range(len(sona)):
        if not list(sona)[i] in kirjavahemargid:
            if list(sona)[i].upper() == list(sona)[i]:
                uussona += list(sona)[i].lower()
                continue
            uussona += list(sona)[i].upper()
        elif not list(sona)[i] == " ":
            uussona += kirjamark
        else:
            uussona += ""
    return uussona

kirjavahemargid = "!?.,&"
print(suurväike("SoNa! ma aeVAStan!"))