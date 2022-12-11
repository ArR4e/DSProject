from random import sample
def bingo():
    kokku = []
    for esimesed in sample(range(1,11),3):
        kokku.append(esimesed)
    if sorted(kokku) == [1,2,3] :
        kokku.clear()
        for esimesed in sample(range(1,11),3):
            kokku.append(esimesed)
    for teised in sample(range(11,21),2):
        kokku.append(teised)
    return (kokku)
    
#print(bingo())
bingo()