def auto_hind(h_h,a):
    if a == 0:
        return h_h
    else:
        return round(auto_hind(h_h*0.8,a-1),2)