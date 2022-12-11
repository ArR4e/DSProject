def sünnikuupäev(ik):
    päev=ik[5:7]
    kuu=ik[3:5]
    aasta=ik[1:3]
    sajand=ik[0:1]
    sajandid=[18, 18, 19, 19, 20, 20]
    aastaajad=["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu=aastaajad[int(kuu)-1]
    sajand=sajandid[int(sajand)-1]
    return(f"{päev}. {kuu} {sajand}{aasta}")