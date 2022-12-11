pikkus = float(input("Sisesta teepikkus koju: "))
fail = open("taksohinnad.txt",encoding="UTF-8")

nimi = ""
odavaim = 99999999

for i in fail:
    a = i.split(",")
    hind = float(a[1])+pikkus*float(a[2])
    if hind < odavaim:
        nimi = a[0]
        odavaim = hind

print(f"Odavaim takso on {nimi}")
    