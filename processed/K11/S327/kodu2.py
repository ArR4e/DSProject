def transponeeriK(maatriks):
    maatriks = maatriks[::-1]
    maatriks2 = [[maatriks[j][i] for j in range(len(maatriks))] for i in range(len(maatriks[0]))]
    maatriks2 = maatriks2[::-1]
    return maatriks2

print(transponeeriK([[4, 31, 67, 99]]))