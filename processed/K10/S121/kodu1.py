def erinevad_sümbolid(line):
    hulk = set()
    for i in line:
        if not i in hulk:
            hulk.add(i)
    return hulk

print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(line):
    hulk = {}
    for i in line:
        if i in hulk:
            hulk[i] +=1 
        else:
            hulk[i] = 1
    return hulk
    
print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(line):
    hulk = {}
    hulk={'Täishäälikud': set(), 'Kaashäälikud' : set(), 'Muud': set()}
    for i in line:
        if i.lower() in "aeiouõäöü":
            if i in hulk:
                hulk['Täishäälikud'].add((i, line.count(i))) 
            else:
                hulk['Täishäälikud'].add((i, line.count(i))) 
        elif i.lower() in "bpdtgkqlsyvnxwcjmhrhfšzž":
            if i in hulk:
                hulk['Kaashäälikud'].add((i, line.count(i)))
            else:
                hulk['Kaashäälikud'].add((i, line.count(i))) 
        else:
            if i in hulk:
                hulk['Muud'].add((i, line.count(i))) 
            else:
                hulk['Muud'].add((i, line.count(i))) 
    return hulk
            
print(grupeeri("sõida tasa üle silla"))
            
        

            