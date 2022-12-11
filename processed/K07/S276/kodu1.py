def poisse_ja_tüdrukuid(x):
    tüdrukud=0
    poisid=0
    for i in x:
        if i[len(x):len(x)+1]=="P":
            poisid += 1
        else:
            tüdrukud += 1
    print([tüdrukud, poisid])
