# 2. Maatriksi transponeerimine kõrvaldiagonaali järgi
# Kirjuta funktsioon transponeeriK, mis võtab argumendina ette maatriksi ning tagastab selle transponeeritud kuju kõrvaldiagonaali järgi.

# Transponeerimine tähendab, et maatriksi read muudetakse veergudeks ja veerud muudetakse ridadeks
# (https://et.wikipedia.org/wiki/Transponeeritud_maatriks). Tavaliselt transponeeritakse maatriksit peadiagonaali järgi,
# aga mõnes olukorras on seda vaja teha ka kõrvaldiagonaali järgi. Kõrvaldiagonaal on see diagonaal, mis ulatub ülemisest paremast
# nurgast alumisse vasakusse nurka.

# Võib eeldada, et etteantud maatriks on transponeeritav, ehk siis kõik read on sama pikad ning kõik veerud on sama pikad.

# >>> transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# [[9, 6, 3], [8, 5, 2], [7, 4, 1]]
# >>> transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])
# [[8, 6, 4, 2], [7, 5, 3, 1]]
# >>> transponeeriK([[4, 31, 67, 99]])
# [[99], [67], [31], [4]]

maatriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

oodatav = [[8, 6, 4, 2],
           [7, 5, 3, 1]]

def transponeeriK(maatriks):
    
    m = []
    ridade_arv = len(maatriks)
    veergude_arv = len(maatriks[0])
    
    for i in range(veergude_arv-1,-1,-1):
        veerud = []
        for j in range(ridade_arv-1,-1,-1):
          veerud.append(maatriks[j][i])
        m.append(veerud)

    return m