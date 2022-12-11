
def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for element in järjend:
        
        uus_järjend = element.split(" ")
        
        if "P" == uus_järjend[-1]:
            m = m + 1
        if "T" == uus_järjend[-1]:
            n = n + 1
    return (m,n)

        
            



        
        