def auto_hind(hind, aastad):
    vaartus = 0
    if aastad != 0:
        uus_hind = hind * 0.8
        auto_hind(uus_hind, aastad - 1)
        return uus_hind
auto_hind(10000.0, 2)
