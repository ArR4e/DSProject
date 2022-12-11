def auto_hind(n, m): #n - hind, m - aastate arv
    if m < 1:
        return n
    else:
        return auto_hind(round(n - (n * 0.2), 2), m - 1)
        #return auto_hind(round(n * (1 - 0.2), 2), m - 1) #teine võimalus
    
#print(auto_hind(10000.0, 6))