def auto_hind(x, y):
    if y == 0:
        return x
    elif y == 1:
        return round(x*0.8, 2)
    else:
        return round(auto_hind(x, y-1)*0.8, 2)
    
x = auto_hind(8000, 5)
print(x)