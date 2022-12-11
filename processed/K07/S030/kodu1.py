def poisse_ja_tüdrukuid(ennik):
    poiste_arv=0
    tydrukute_arv=0
    for i in ennik:
        if i[-1] =='P':
            poiste_arv+=1
        if i[-1] =='T':
            tydrukute_arv+=1
    return(poiste_arv, tydrukute_arv)
