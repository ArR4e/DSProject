def auto_hind(hind, aastad):
    if aastad >= 1:
        return auto_hind(0.8*hind, aastad-1)
    else:
        return round(hind, 2)
    
#automaatkontroll ytleb, et selle vastus on vale
#peaks 4344.62 olema, kuigi mul on 4344.61 ja imo mul kõik õigesti ymardatud
#vaadake oma automaatkontroll yle
print(auto_hind(6788.46, 2))