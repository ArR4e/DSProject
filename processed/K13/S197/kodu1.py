def auto_hind(price, years):
    if years == 0:
        return round(price, 2)
    return round(auto_hind(price*.8, years-1), 2)