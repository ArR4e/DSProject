def moos(s, v, k):
    karp = 0
    for i in range(s):
        if k-5>=0:
            karp += 1
            k -= 5
    if k<=v:
        karp += k
    else:
        karp = -1
    return karp

print(moos(2,6,14))