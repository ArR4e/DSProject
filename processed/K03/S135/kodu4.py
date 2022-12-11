# Kirjuta programm, mis loeb tekstifailist kinganumbrid.txt sisse
# EU kinganumbrid ja kuvab ekraanile vastavad jalalaba
# pikkused sentimeetrites ümardatuna täisarvuks.

f = open('kinganumbrid.txt')

while True:
    kinganumber = f.readline()
    if kinganumber == '':
        break
        f.close()
    try:    
        pikkus = round(2/3 * (float(kinganumber) - 2))
        print(pikkus)
    except:
        print('Vigane sisend')

