# 1. Kasutatud auto hind rekursiivselt

# m - auto hind
# n - aastate arv

def auto_hind(m, n):
    if n == 0:
        return m
    else:
        return round(auto_hind(m, n - 1) * 80 / 100, 2)
   
#print(auto_hind(10000.0, 5))
