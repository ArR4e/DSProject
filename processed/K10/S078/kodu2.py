jär_element_x = 'XXX'
jär_element_o = 'OOO'
X = 0
O = 0
def võitja(maatriks):
    sõnastik = {}
    horisontaalne(maatriks)
    vertikaalne(maatriks)
    põhidiagonaalil(maatriks)
    kõrvaldiagonaalil(maatriks)
    sõnastik['O'] = O
    sõnastik['X'] = X
    return sõnastik


def horisontaalne(maatriks):
    global O
    global X
    for i in range(len(maatriks)):
        for j in range(2):
            rida = maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]
            if rida.strip() == jär_element_x:
                X += 1
            elif rida.strip() == jär_element_o:
                O += 1
                
def vertikaalne(maatriks):
    global O
    global X
    for j in range(len(maatriks)):
        for i in range(2):
            rida = maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]
            if rida.strip() == jär_element_x:
                X += 1
            elif rida.strip() == jär_element_o:
                O += 1
                
def põhidiagonaalil(maatriks):
    global O
    global X
    for i in range(2):
        for j in range(2):
            rida = maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]
            if rida.strip() == jär_element_x:
                X += 1
            elif rida.strip() == jär_element_o:
                O += 1

def kõrvaldiagonaalil(maatriks):
    global O
    global X
    for i in range(2):
        for j in range(2):
            rida = maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]
            if rida.strip() == jär_element_x:
                X += 1
            elif rida.strip() == jär_element_o:
                O += 1