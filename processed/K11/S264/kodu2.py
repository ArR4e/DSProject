#Kirjuta funktsioon transponeeriK, mis võtab argumendina ette maatriksi ning tagastab selle transponeeritud kuju kõrvaldiagonaali järgi.
#Transponeerimine tähendab, et maatriksi read muudetakse veergudeks ja veerud muudetakse ridadeks
#(https://et.wikipedia.org/wiki/Transponeeritud_maatriks). Tavaliselt transponeeritakse maatriksit peadiagonaali järgi, aga mõnes
#olukorras on seda vaja teha ka kõrvaldiagonaali järgi. Kõrvaldiagonaal on see diagonaal, mis ulatub ülemisest paremast nurgast alumisse
#vasakusse nurka.
#Võib eeldada, et etteantud maatriks on transponeeritav, ehk siis kõik read on sama pikad ning kõik veerud on sama pikad.
# 
maatriks = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
def transponeeriK(maatriks):
    järjend = []
    for i in range(len(maatriks[0])):
        rida = []
        for j in range(len(maatriks)):
            element = maatriks[j][i]
            rida.append(element)
        järjend.append(rida)
    return järjend


print(transponeeriK(maatriks))

# maatriks = [[1,2,3],
#            [3,4,5]]
# for i in range(2,-1,-1):
#     for j in range(1,-1,-1):
#         print(maatriks[j][i], end=' ')
#     print()