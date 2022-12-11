def erinevad_sümbolid(s):
    h = set()
    for t in s:
        h.add(t)
    return h

def sümbolite_sagedus(o):
    a = erinevad_sümbolid(o)
    s = {}
    for t in a:
        l=o.count(t)
        s[t]=l
    return s
    
def grupeeri(o):
    kaash = "bdfghjklmnprsšqzžctvwxyBDFHGHJKLQMNPRCSŠZXYŽTVW"
    täish = "aeiouöäõüAEIOUÕÄÖU"
    x = {"Täishäälikud":None,
         "Kaashäälikud":None,
         "Muud":None}
    u = sümbolite_sagedus(o)
    t = set()
    k = set()
    m = set()
    for i in u:
        if i in kaash:
            k.add((i,u[i]))
        elif i in täish:
            t.add((i,u[i]))
        else:
            m.add((i,u[i]))
    x["Täishäälikud"] = t
    x["Kaashäälikud"] = k
    x["Muud"] = m
    return x

    