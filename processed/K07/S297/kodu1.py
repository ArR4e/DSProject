järjend = ['Anna T', 'Peeter P', 'Tiiu T', 'Karl P', 'Matilde T']

def poisse_ja_tüdrukuid(järjend) :
    töödeldud_järjend = []
    for i in järjend :
        töödeldud_järjend += i.split()  
    poisse = töödeldud_järjend.count('P')
    tüdrukuid = töödeldud_järjend.count('T')
    return (poisse, tüdrukuid)