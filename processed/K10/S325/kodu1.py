def erinevad_sümbolid(j):
    e=set(j)
    return e
def sümbolite_sagedus(j):
    s={}
    for char in j:
        if char not in s:
            s[char]=1
        else:
            s[char]+=1
    return s
def grupeeri(j):
    t={}
    t["Täishäälikud"]=set()
    t["Kaashäälikud"]=set()
    t["Muud"]=set()
    s=sümbolite_sagedus(j)
    for key in s:
        if key in "aeiouõüäö":
            t["Täishäälikud"].add((tuple((key,s[key]))))
        elif key in "qwrtyplkjhgfdszxcvbnm":
            t["Kaashäälikud"].add((tuple((key,s[key]))))
        else:
            t["Muud"].add((tuple((key,s[key]))))
    return t