def auto_hind(hind, aastad):
    if aastad > 0:
        hind *= 0.8
        aastad -= 1
        return auto_hind(hind, aastad)
    elif aastad == 0:
        return round(hind, 2)

print(auto_hind(8000.0, 5))