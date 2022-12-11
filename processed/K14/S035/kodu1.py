def rek_abs(järjend):
    järjend2=järjend.copy()
    for i in range(len(järjend2)):
        if isinstance(järjend2[i], list)==False:
            if järjend2[i]>=0:
                continue
            else:
                järjend2[i]=0-järjend2[i]
        else:
            järjend2[i]=rek_abs(järjend2[i])
    return(järjend2)