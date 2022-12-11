e=["Mati T","Kati T","Siim Aleksander P","Jüri P","Veroonika T"]
def poisse_ja_tüdrukuid(järjend):
    p=0
    t=0
    for rida in järjend:
        i=rida[-1]
        print(i)
        if i=="P":
            p=p+1
        elif i=="T":
            t=t+1
    return (p,t)
