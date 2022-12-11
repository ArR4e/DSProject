def auto_hind(price, n):
    if n == 0:
        return round(price, 2)
    else:
        return round(auto_hind(price - (round(price * 0.2, 2)), n-1), 2)
    
print(auto_hind(6788.46, 2))