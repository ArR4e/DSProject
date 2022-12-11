h = set()
s = {}
j = []
def erinevad_sümbolid(sümbolid):
    for i in range(len(sümbolid)):
        h.update(sümbolid)
    return(h)

def sümbolite_sagedus(sümbolid):
    erinevad_sümbolid(sümbolid)
    for i in h:
        j.append(i)
    for täht in j:
        s[täht] = s.get(täht, 0) + 1
    return(s)

        