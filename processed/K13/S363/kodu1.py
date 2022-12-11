#iga aasta 20% väiksem hind

def auto_hind(hind, aastaid):
    if aastaid <= 0:
        return round(hind,2)

    else:
        return auto_hind(round(hind*0.8,2), aastaid-1)
