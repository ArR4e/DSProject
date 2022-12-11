def moos(suured, väiksed, kogus):
    while True:
        if kogus == 0:
            return 0
            break
        if 1 <= int(kogus) <= 4 and väiksed>= kogus:
            suured = 0
            väiksed = kogus
            return väiksed
        if suured == 0 and väiksed >= kogus:
            väiksed = kogus//1
            return väiksed + suured
        if väiksed == 0 and kogus < 5:
            return -1
        if int(kogus//5):
            if suured > kogus//5 and väiksed >= kogus% 5:
               suured = kogus//5
               kogus = kogus % 5
               väiksed = kogus//1
               return suured + väiksed
            if suured <= kogus//5 and väiksed >= kogus -suured*5:
                suured = suured
                kogus = kogus - suured*5
                väiksed = kogus//1
                return suured + väiksed
            if suured == kogus//5 and kogus%5 == 0:
                suured = suured
                väiksed = 0
                return suured
            else:
                return -1
                break
    
