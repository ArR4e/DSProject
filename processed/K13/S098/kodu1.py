def auto_hind(auto, aeg):
    if aeg == 0:
        return (round(auto, 2))
    else:
        return auto_hind((0.8*auto), aeg-1)
    
auto_hind(10000, 2)