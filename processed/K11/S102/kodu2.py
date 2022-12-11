import copy
def lenx(a):
    try:
        return len(a)
    except:
        return 1


def transponeeriK(mat):
    koopia=copy.deepcopy(mat)
    mat=[]
    for m in range(lenx(koopia[0])):
        mat.append([])
        for n in range(lenx(koopia)):
            if lenx(koopia)==1:
                mat[m].append(koopia[0][lenx(koopia[0])-m-1])
            
            elif lenx(koopia[0])==1:
                mat[m].append(koopia[lenx(koopia)-n-1][0])
                
            else:
                mat[m].append(koopia[lenx(koopia)-n-1][lenx(koopia[0])-m-1])
    return mat
#transponeeriK([[1], [2], [3], [4], [5], [6], [7], [8], [9]])