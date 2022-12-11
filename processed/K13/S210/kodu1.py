def auto_hind(a,b):
    if b == 0:
        return round(a, 2)
    vastus = a * 0.8
    return (auto_hind(vastus, b - 1))

print(auto_hind(10000, 6))