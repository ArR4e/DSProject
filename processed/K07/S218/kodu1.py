def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for element in järjend:
        a = element.split()
        sugu = a[-1]
        if sugu == "P":
            poisid = poisid +1
        if sugu == "T":
            tüdrukud = tüdrukud +1

    return (poisid, tüdrukud)

print(poisse_ja_tüdrukuid([]))
