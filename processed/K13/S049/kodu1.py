def auto_hind(a, b):
    while b > 0:
        hind = round((a*0.8), 2)
        b -= 1
        a = hind
        
    else:
        print(round(a, 2))
        
        