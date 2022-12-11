def transponeeriK(maatriks):
    return [list(rida) for rida in zip(*maatriks[::-1])][::-1]

#Kõrvaldiagonaali järgi transponeerimiseks peame lihtsalt
#maatriksi selle diagonaali järgi pöörama, ehk maariks[::-1] ja
#pärast veelkord [::-1]