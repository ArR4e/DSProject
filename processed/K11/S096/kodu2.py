# Maatriksi transponeerimine kõrvaldiagonaali järgi

def transponeeriK(maatriks):
    maatriks_T = []
    for i in range(len(maatriks[0])):  #Tsükkel käib läbi maatriksi read
        vahejärjend = []
        for j in range(len(maatriks)):  #Tsükkel käib läbi maatriksi veerud
            element = maatriks[len(maatriks)-j-1][len(maatriks[0])-i-1]
            vahejärjend.append(element)
        maatriks_T.append(vahejärjend)

    return maatriks_T

maatriks = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
uus_maatriks = transponeeriK(maatriks)

for i in maatriks:
    print(i)
print()
for i in uus_maatriks:
    print(i)