def auto_hind(hind, aastate_arv):
    if aastate_arv == 0:
        return hind
    else:
        return round(auto_hind(hind * 0.8, aastate_arv - 1), 2)
        #automaatkontrollile ei meeldi ymardatud vastus :(

print(auto_hind(10000, 6))