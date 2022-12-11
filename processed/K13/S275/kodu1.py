def auto_hind(x, y):
    if y == 0:
        return x
    else:
        vastus = auto_hind(x * 0.8, y - 1) 
        return round(vastus, 2)
