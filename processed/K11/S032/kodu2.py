def transponeeriK(maatriks):
    m_ridu = len(maatriks)
    m_veerge = len(maatriks[0])
    tm = []
    for m in range(m_veerge): 
        tm.append([0]*m_ridu)
    for i, rida in enumerate(maatriks):
        for j, arv in enumerate(rida):
            tm[m_veerge-j-1][m_ridu-i-1] = arv
    return tm

transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])