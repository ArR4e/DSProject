def auto_hind(h,a):
    return h if a == 0 else round(auto_hind(h,a-1)*0.8,2)
print(auto_hind( 6788.46 ,2))