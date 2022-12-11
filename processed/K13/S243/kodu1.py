#1. kasutatud auto hind rekursiivselt

def auto_hind(hind, vanus):
    if vanus==0:
        return hind
    return round((auto_hind(hind, vanus-1)*0.8), 2)

print(auto_hind(10000, 5))
print(auto_hind(10000, 1))
print(auto_hind(8000, 5))