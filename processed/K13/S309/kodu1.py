def auto_hind(price, years):
    if years == 0:
        return price
    else:
        return auto_hind(round(price*0.8, 2), years-1)
