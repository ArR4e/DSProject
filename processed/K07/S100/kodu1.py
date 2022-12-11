def poisse_ja_tüdrukuid(arr):
    poisid = 0
    tydrukud = 0
    for i in arr:
        if i[-1] == "P":
            poisid += 1
        else:
            tydrukud += 1
    return (poisid, tydrukud)