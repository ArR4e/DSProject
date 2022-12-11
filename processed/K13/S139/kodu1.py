def auto_hind(hind,a):
    if a == 0:
        return (hind)
    else:
        return auto_hind(round(hind-(hind*0.2),2),a-1)


print(auto_hind(10000.0, 111))