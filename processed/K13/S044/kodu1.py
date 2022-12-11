def auto_hind(alghind, kordus):
    while kordus >= 1:
        alghind = (alghind/100)*80
        alghind = round(alghind, 2)
        kordus -= 1
    return alghind