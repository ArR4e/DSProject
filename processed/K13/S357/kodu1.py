def auto_hind(price, yr):
    if yr == 0:
        return price
    else:
        price = round(price - price * 0.2, 2)
        return auto_hind(price, yr-1)