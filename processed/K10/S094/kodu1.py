
def erinevad_sümbolid(s):
    erinevad = set()
    for t in s:
        if t == ' ':
            pass
        else:            
            erinevad.add(t)
    print(erinevad)
    
erinevad_sümbolid("ssadas   asdas s 3")