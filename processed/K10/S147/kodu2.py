def võitja(maatriks):
    väljund = {}
    for mitmes_rida, rida in enumerate(maatriks):
        for mitmes_el, el in enumerate(rida):
            if el == "O" or el == "X":
                if mitmes_el <= 1 and rida[mitmes_el+1] == el and rida[mitmes_el+2] == el:
                    väljund[el] = väljund.get(el,0)+1
                if mitmes_rida <= 1 and maatriks[mitmes_rida+1][mitmes_el] == el and maatriks[mitmes_rida+2][mitmes_el] == el:
                    väljund[el] = väljund.get(el,0)+1
                if mitmes_rida <= 1 and mitmes_el <= 1:
                    if maatriks[mitmes_rida+1][mitmes_el+1] == el and maatriks[mitmes_rida+2][mitmes_el+2] == el:
                        väljund[el] = väljund.get(el,0)+1
                if mitmes_el >= 2 and mitmes_rida <= 1:
                    if maatriks[mitmes_rida+1][mitmes_el-1] == el and maatriks[mitmes_rida+2][mitmes_el-2] == el:
                        väljund[el] = väljund.get(el,0)+1
    if "O" not in väljund: väljund["O"] = 0
    if "X" not in väljund: väljund["X"] = 0
    return väljund
print(võitja([['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]))