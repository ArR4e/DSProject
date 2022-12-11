import math
def moos(a, b, c):
    kogus = int(c)
    väike = int(b)
    suur = int(a)
    suuri = math.floor(kogus/5)
    väikeseid = kogus-suuri*5
    kokku = suuri + väikeseid
    if suuri*5 + väikeseid < kogus or väikeseid > väike or kogus == 0 or suuri > suur:
        return -1
    else:
        return kokku
moos(3, 3, 8)
