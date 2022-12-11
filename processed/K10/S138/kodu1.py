def erinevad_sümbolid(sisend):
    hulk = set()
    sisend = list(sisend)
    for i in sisend:
        if i not in hulk:
            hulk.add(i)
    return hulk

def sümbolite_sagedus(sisend):
    hulk = {}
    sisend = list(sisend)
    for i in sisend:
        if i not in hulk:
            hulk[i] = 1
        else:
            hulk[i]+=1
    return hulk
            
def grupeeri(sisend):
    hulk = {}
    täishäälikud = list("aeiouõäöüAEIOUÕÖÖÜ")
    kaashäälikud = list("bdfghjklmnprsztvqxwcyBDFGHJKLMNPRSZTVQXWCY")
    täishäälikute_hulk = set()
    kaashäälikute_hulk = set()
    muud_hulk = set()
    sisend = list(sisend)
    for i in täishäälikud:
        if i in sisend:
            kogus = sisend.count(i)
            tulem = (i,kogus)
            täishäälikute_hulk.add(tulem)
            try:
                while True:
                    sisend.remove(i)
            except:
                pass             
    for i in kaashäälikud:
        if i in sisend:
            kogus = sisend.count(i)
            tulem = (i,kogus)
            kaashäälikute_hulk.add(tulem)
            try:
                while True:
                    sisend.remove(i)
            except:
                pass
    for i in sisend:
        kogus = sisend.count(i)
        tulem = (i,kogus)
        muud_hulk.add(tulem)
        try:
            while true:
                sisend.remove(i)
        except:
            pass
    hulk["Täishäälikud"] = täishäälikute_hulk
    hulk["Kaashäälikud"] = kaashäälikute_hulk
    hulk["Muud"] = muud_hulk
    return hulk
        