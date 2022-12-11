
def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for i in järjend:
        if i[-1] == "P" and i[-2] == " ":
            poisid += 1
        elif i[-1] == "T" and i[-2] == " ":
            tüdrukud += 1           
    return (poisid, tüdrukud)
