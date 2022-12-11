f=open("kinganumbrid.txt")
i=0
ridade_arv=0
for rida in f:         # Mul ei tulnud hetkel paremat mõtet ridade arvu saamiseks.
    if rida!="":       # For tsüklit mäletan ma kursuselt "Tehnoloogia tarbijast loojaks".
        ridade_arv +=1
f.close()
f=open("kinganumbrid.txt")
while i < ridade_arv:
    try:
        kinganumber=float((f.readline()))
        pikkus = 2/3 * (kinganumber-2)
        print(round(pikkus))
    except:
        print("Vigane sisend!")
    i+=1