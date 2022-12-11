sõne="elu on ilus!#%%"
t="aeiouõäöüAEIOUÕÄÖÜ"
k="bdfghjklmnpržšsztvBDFHGKJLMNPRŽŠSZTV"
def erinevad_sümbolid(sõne):
    hulk=set(sõne)
    return hulk
def sümbolite_sagedus(sõne):
    sõnastik={}
    split_string=[]
    n=1
    for index in range(0, len(sõne), n):
        split_string.append(sõne[index : index +n])
    for i in split_string:
        c=split_string.count(i)
        sõnastik[i]=c
    return sõnastik
def grupeeri(sõne):
    sõnastik={}
    sõnastik["Täishäälikud"]=set()
    sõnastik["Kaashäälikud"]=set()
    sõnastik["Muud"]=set()
    a=sümbolite_sagedus(sõne)
    for võti in a:
        if võti in t:
            sõnastik["Täishäälikud"].add((võti, a[võti]))
        if võti in k:
            sõnastik["Kaashäälikud"].add((võti, a[võti]))
        else:
            sõnastik["Muud"].add((võti, a[võti]))
#     #sth
    return sõnastik
print(erinevad_sümbolid(sõne))
a=set("absaa")
print(a)
sümbolite_sagedus(sõne)
print(grupeeri(sõne))