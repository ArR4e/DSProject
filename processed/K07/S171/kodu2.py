andmed = []

with open("taksohinnad.txt", "r") as f:
    for rida in f:
        a = rida.strip().split(",")
        andmed.append(a)
try:
    s = float(input("Sisesta tee pikkus kilomeetrites:"))
    odavh = float(andmed[0][1]) + float(andmed[0][2])*s
    odavn = ""
    for i in andmed:
        if float(i[1]) + float(i[2])*s <= odavh:
            odavh = float(i[1]) + float(i[2])*s
            odavn = i[0]
        
    print(f"Kõige odavam on {odavn}")
    
except:
    print("Kõige odavam on")
