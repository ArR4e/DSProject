def moos(a, b, c):
    smaht = a * 5
    ## Esimene tingimus tagab selle, et jääk oleks ilma koma kohta, ning moos mahuks täpselt krapidesse
    ## Teine tingimus kontrollib, kas karpide mahutuvus on piisavalt suur moosi koguse jaoks
    ## Kolmas tingimus kontrollib, et jäägi arv oleks väiksem võrdne 1kg karpide arvuga
    if c % 5 - (int(c % 5)) == 0 and smaht + b >= c and c % 5 <= b:
        if smaht >= c:
            s = int(c / 5)
            v = c % 5
            return s+v
        elif smaht < c:
            j = c - smaht
            m = int((c - j) / 5)
            return j + m
    else:
        return -1