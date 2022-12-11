def auto_hind(alg, t):
    if t-1 >= 0:
        hind = auto_hind(round(alg*0.8, 2), t-1)
        return hind
    else:
        return alg
print(auto_hind(6788.46, 2))