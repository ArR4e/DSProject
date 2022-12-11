def f(hind, aastad):
    if aastad == 0:
        return hind
    else:
         return round(f(0.8 * hind, aastad - 1), 2)
         
         
print(f(8000,5))