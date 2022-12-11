
def moos(kg_5, kg_1, kg_sum):
    karpide_arv = 0
    
    while True:
        if kg_5 > 0 and kg_sum - 5 >= 0:    # Kontrolli, kas saab kasutada 5kg
            karpide_arv += 1                # karpi ja pane see kirja, kui saab.
            kg_sum -= 5
            kg_5 -= 1
        else:
            break
    
    while True:
        if kg_1 > 0 and kg_sum - 1 >= 0:    # Kontrolli, kas saab kasutada 1kg
            karpide_arv += 1                # karpi ja pane see kirja, kui saab.
            kg_sum -= 1
            kg_1 -= 1
        else:
            break
        
    if kg_sum != 0:         # Kui karpidest ei piisa, muuda karpide_arv = -1
        karpide_arv = -1
        
    print(karpide_arv)
    return(karpide_arv)

