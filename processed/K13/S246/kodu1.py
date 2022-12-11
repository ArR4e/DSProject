def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        uus = hind / 100 * 20
        vastus = auto_hind(round(hind - uus, 2), aastad - 1)
        return vastus
print(auto_hind(6788.46, 2))