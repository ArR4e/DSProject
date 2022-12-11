def auto_hind(value, year):
    if year == 0:
        return round(value, 2)
    else:
        return auto_hind(value*0.8, year-1)

print(auto_hind(10000.0, 6))