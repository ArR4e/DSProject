#defineerin funktsiooni moos, mis võtab 3 argumenti
def moos(suur, väike, kogus):
    karpe = 0
    while True:
        if kogus == 0:#kui kõik kogus on karpidesse ära mahutatud, tagastab vaja minevate karpide arvu
            return karpe
        if suur > 0:#Kui suuri karpe on veel alles
            if kogus % 5 == 0:#Kui kogus mahub täpselt suurde karpi
                kogus -= 5
                suur -=1
                karpe += 1#vaja minevate karpide arv suureneb 1 võrra
                continue
        if väike > 0:#kui väikseid karpe on veel alles
            kogus -= 1
            väike -= 1
            karpe += 1#vaja minevate karpide arv suureneb 1 võrra
        else:
            return -1#juhul kui väikeseid karpe pole ja suuri pole või nendesse ei mahu, siis tagastab -1