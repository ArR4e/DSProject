def auto_hind(x,y):
    if y==0:
        return round(x,2)
    else:
        return round(auto_hind(x*0.8,y-1),2)
print(auto_hind(10000,5))