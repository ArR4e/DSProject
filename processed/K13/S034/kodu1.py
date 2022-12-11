def auto_hind(hind,aastad):
    if aastad == 0:
        #ümardame kahe komakohani
        return(round(hind,2))
    else:
        #arvestame, et auto kaotab iga aasta 20% oma väärtusest
        #ehk säilitab 80% oma väärtusest
        hind *= 0.8
        aastad -=1
        return auto_hind(hind,aastad)