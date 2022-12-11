km = float(input("Kaugele sõidame? "))

f = open("taksohinnad.txt", encoding = "UTF-8")

odavaim_hind = 10.0**10
odavaim_takso = ''
for line in f:
    rida = line.strip().split(',')
    hind = float(rida[1]) + km*float(rida[2])
    if hind < odavaim_hind:
        odavaim_hind = hind
        odavaim_takso = rida[0]
    
print("Kõige odavam on", odavaim_takso)

f.close()