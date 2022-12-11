#a = [[1, 2],
     #[3, 4],
     #[5, 6]]
def transponeeriK(a) :
    b = []
    for i in range(len(a)-1,-1,-1):
        index_b = 0
        for j in range(len(a[0])-1,-1,-1):
            if i == len(a)-1:
                b_rida = []
                b_rida.append(a[i][j])
                b.append(b_rida)
                #print(b)
            else:
                b[index_b].append(a[i][j])
                index_b += 1
    return b
