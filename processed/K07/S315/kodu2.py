f = open("taksohinnad.txt", "r")
km = float(input("Kaugel kodu on? "))
nimi = ""
hind = 0
parim_hind = 1000000000000
parim_nimi = ""
while True:
    rida = f.readline().strip().split(",")
    jär = [rida]
    if rida == [""]:
        break
    for i in jär:
        nimi = i[0]
        hind = float(i[1]) + km*float(i[2])
        if parim_hind > hind:
            parim_hind = hind
            parim_nimi = nimi
    
    

print(f"Odavaim takso on {parim_nimi}")
