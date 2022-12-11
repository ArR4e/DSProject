def moos(karp_s_arv, karp_v_arv, kogus):
    i = 0
    a = 0
    while i < kogus:
        if karp_s_arv > 0 and (kogus - i) >= 5:
            karp_s_arv -= 1
            i += 5
            a += 1
        elif karp_v_arv > 0 and (kogus - i) >= 1:
            karp_v_arv -= 1
            i += 1
            a += 1
        elif i < kogus:
            return -1
    return a