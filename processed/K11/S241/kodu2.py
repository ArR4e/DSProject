
# teeb suurema osa transponeerimisest ära, valedeks jäävad kaks kohta - indeksid 00 ja 22 - teised vahetavad kohad nii nagu peab

maatriks = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

def transponeeri(mx):
    matrix = [[0,0,0], [0,0,0], [0,0,0]]
    for ele1 in range(len(mx)):
        for ele2 in range(len(mx)):
            if ele1 != ele2:
                matrix[ele2][ele1] = mx[len(mx)-ele1-1][len(mx)-ele2-1]
            else:
                matrix[ele2][ele1] = mx[ele2][ele1]
    return matrix
print(transponeeri(maatriks))

