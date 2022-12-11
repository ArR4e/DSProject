teep = int(input("Sisesta teepikkus kilomeetrites: "))
def odavaim_takso(teep):
    odavaim = 1000000000000.0
    odavaim_nimi = ''
    with open("taksohinnad.txt", 'r') as f:
        for i in f.readlines():
            i = i.rstrip().split(',')
            calculation = float(i[1]) + float(i[2]) * teep
            if  calculation < odavaim:
                odavaim = float(i[1]) + float(i[2]) * teep
                odavaim_nimi = i[0]
    print(odavaim_nimi)



odavaim_takso(teep)