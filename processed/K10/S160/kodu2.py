# Teeme mingi tühja hulga, et lugeda O-sid ja X-e,
# mida täidetakse siis, kui reas või veerus esineb O või X
tripstrapstrull = {"O" : 0, "X" : 0}

# Inspiratsiooni ka : https://stackoverflow.com/questions/43082149/simple-way-to-count-number-of-specific-elements-in-2d-array-python

# Edasi tuleks lugeda ära, kas vastav sümbol esineb reas/veerus/diagonaalis
# ning siis liita see hulgale tripstrapstrull
# Võtan muutuja i ridade tähistamiseks, j veergude tähistuseks, k diagonaali jaoks.
# Muster on ainult siis, kui korvuti on 3 & 4(numbriline tähistus juhendis antud 1 & 2) sama symbolit
# (horisontaalselt, vertikaalselt, diagonaalselt)

def võitja(maatriks):

    ### Horisontaalseks kombinatsiooni lugemiseks 
    
    for i in maatriks:
        if i.count('O') == 3 :
            tripstrapstrull['O'] += 1
        if i.count('O') == 4:
            tripstrapstrull['O'] += 2
        if i.count('X') == 3 :
            tripstrapstrull['X'] += 1
        if i.count('X') == 4:
            tripstrapstrull['X'] += 2
    return tripstrapstrull

võitja([['X','X','X',' '],[' ','O',' ',' '],[' ',' ','O',' '],[' ',' ',' ','O']])