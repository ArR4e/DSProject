a = open('taksohinnad.txt', 'r', encoding='UTF-8')

km = float(input("Sisesta mitu kilomeetrit tahad sõita: "))
taksode_hinnad = []
taksode_nimed = []
if a.read() =='':
    print('')

else:
    a.seek(0, 0)
    for rida in a:
        if rida == '':
            break
        järjend = rida.strip().split(",")
        hind = float(järjend[1]) + km * float(järjend[2])
        taksode_hinnad.append(hind)
        taksode_nimed.append(järjend[0])
    madalaim_hind_indeks = taksode_hinnad.index(min(taksode_hinnad))
    madalaim_takso = taksode_nimed[madalaim_hind_indeks]
    print("Kõige odavam on " + str(madalaim_takso))
    
a.close()
