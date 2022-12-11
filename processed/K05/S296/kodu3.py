def moos(suur,väike,kogus):
    if kogus % 5 == 0 and kogus // 5 <= suur and suur != 0:
        return kogus // 5
    elif suur == 0 and väike >= kogus:
        return kogus
    elif kogus % 5 == 0 and kogus // 5 > suur and kogus - ((kogus // 5) * 5) <= väike and (suur * 5 + väike) >= kogus and väike != 0 and suur != 0:
        return kogus - (suur * 5) + suur
    elif kogus % 5 != 0 and kogus // 5 <= 2  and kogus - ((kogus // 5) * 5) <= väike and väike != 0 and suur != 0:
        return kogus - ((kogus // 5)*5) + (kogus // 5)
    else:
        return (-1)
print(moos(1,2,10))