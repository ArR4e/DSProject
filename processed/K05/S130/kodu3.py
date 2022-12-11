# suured = int(input("Sisesta Suurte karpide arv: "))
# väiksed = int(input("Sisesta väikeste karpide arv: "))
# moosi = int(input ("Sisesta moosi kogus: "))
def moos(suured, väiksed, moosi):
    suuri_kulus = 0
    väikseid_kulus = 0
    if 5*suured+väiksed < moosi:
        return -1
    else:
        while suured > 0 and moosi >= 5:
            moosi = moosi - 5
            suured = suured - 1
            suuri_kulus += 1
        else:
            while väiksed > 0 and moosi >= 1:
                moosi = moosi - 1
                väiksed = väiksed - 1
                väikseid_kulus += 1
            if moosi == 0:
                summa = suuri_kulus+väikseid_kulus
                return summa
            else:
                return -1
            