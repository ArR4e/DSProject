def poisse_ja_tüdrukuid(järjend):
    s = ','.join(järjend)
    poisse = s.count(' P')
    tüdrukuid = s.count(' T')
    return(poisse,tüdrukuid)