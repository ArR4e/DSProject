
def auto_hind(price, years):
    if years == 0:
        return price
    else:
        return round(0.8 * auto_hind(price, years-1), 2)
