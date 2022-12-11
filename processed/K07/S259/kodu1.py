def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for i in järjend:
        if i[-1] == 'T': #teeb kindlaks, et järjendi viimane liige vastaks tingimusele
            tüdrukuid +=1
        elif i[-1] == 'P':
            poisse += 1
    if poisse == 0 and tüdrukuid == 0:
        return (0, 0)
    return (poisse, tüdrukuid)