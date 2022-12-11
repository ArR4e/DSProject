def auto_hind(autohind, aastad):
    if aastad < 1:
        return autohind
    else:
        uushind = autohind * (1 - (20/100))
        return round(auto_hind(uushind, aastad - 1), 2)