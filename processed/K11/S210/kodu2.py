def transponeeriK(a):
    a.reverse()
    for el in a:
        el.reverse()
    zipped_rows = zip(*a)
    transponeeri_maatriks = [list(row) for row in zipped_rows]
    return transponeeri_maatriks