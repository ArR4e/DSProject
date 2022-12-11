#https://www.codegrepper.com/search.php?answer_removed=1&q=transpose%20matrix%20in%20python%20without%20numpy
def transponeeriK(maatriks):
    uus = []
    for i in reversed(range(len(maatriks[0]))):
        rida = []
        for j in reversed(range(len(maatriks))):
            rida.append(maatriks[j][i])
        uus.append(rida)
    return uus
     
print(transponeeriK([[4, 31, 67, 99]]))