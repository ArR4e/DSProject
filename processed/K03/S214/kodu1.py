print("Tere! Olen maksuvaba tulu arvutaja.")

while True:
    aasta_tulu = float(input("Sisesta aastatulu: "))
    if aasta_tulu>0:
        if aasta_tulu<=6000:
            maksuvaba_tulu = aasta_tulu
        elif 6000< aasta_tulu <=14400:
            maksuvaba_tulu = 6000
        elif 14400< aasta_tulu <=25200:
            maksuvaba_tulu = 6000-6000/10800*(aasta_tulu-14400)
        else:
            maksuvaba_tulu = 0
    
        break
    else:
        print("Sisestasid valesti, proovi uuesti.")
print("Maksuvaba tulu on "+str(round(maksuvaba_tulu, 2))+" eurot.")