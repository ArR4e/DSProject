f = open("taksohinnad.txt", encoding="UTF-8")
s = []
nimi = []
hind = []

for line in f:
    s += line.strip().split(",")
k = float(input("Sisesta kilomeetrite arv: "))
    
y = 0
while y < len(s):
    l = s[y].replace(' ','')
    if l.isalpha() == True:
        nimi.append(s[y])
    else:
        if not s[y].isalpha() == True:
            hind.append(float(s[y]) + float(s[y+1])*k)
            y += 1
    y += 1
try:
    miinimum = min(hind)
    indeks = hind.index(miinimum)
    print("Kõige odavam on "+nimi[indeks]+".")
except:
    print("Ei ole informatsiooni")
f.close()