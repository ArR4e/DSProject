#Maatriksi transponeerimine kõrvaldiagonaali järgi

def transponeeriK(maatriks):
    return [list(rida[::-1]) for rida in list(zip(*maatriks))][::-1]