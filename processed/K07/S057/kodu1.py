#järjend = ["Karl P", "Annabel T", "Charles P", "Eva T", "Jürgen P"]

def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tydrukute_arv = 0
    for elem in järjend:
        if elem.endswith(" P"):
            poiste_arv +=1
        elif elem.endswith(" T"):
            tydrukute_arv +=1
    return (poiste_arv, tydrukute_arv)
