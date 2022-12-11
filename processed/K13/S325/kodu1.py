def auto_hind(h,a):
    if a==0:
        return h
    else:
        return round(auto_hind(h,a-1)*0.8,2)